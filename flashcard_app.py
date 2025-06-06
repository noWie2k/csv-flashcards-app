import tkinter as tk
from tkinter import messagebox
import csv
import os

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcards")
        self.master.geometry("1600x900")
        self.dark_mode = True

        # Farben für Light- und Dark-Mode
        self.light_bg = "white"
        self.light_fg = "black"
        self.dark_bg = "#2e2e2e"
        self.dark_fg = "white"

        # Top-Frame für Dropdown und Dark-Mode-Button
        top_frame = tk.Frame(master)
        top_frame.pack(fill="x", padx=10, pady=5)

        # Dropdown: verfügbare CSV-Dateien im aktuellen Verzeichnis
        self.csv_files = [f for f in os.listdir(os.getcwd()) if f.lower().endswith(".csv")]
        if not self.csv_files:
            messagebox.showerror("Fehler", "Keine CSV-Dateien im Verzeichnis gefunden.")
            master.destroy()
            return

        self.selected_csv = tk.StringVar(master)
        self.selected_csv.set(self.csv_files[0])

        dropdown_label = tk.Label(top_frame, text="CSV-Datei:", font=("Arial", 12))
        dropdown_label.pack(side="left")

        self.csv_menu = tk.OptionMenu(top_frame, self.selected_csv, *self.csv_files, command=self.change_csv)
        self.csv_menu.config(font=("Arial", 12))
        self.csv_menu.pack(side="left", padx=(5, 20))

        self.mode_button = tk.Button(
            top_frame,
            text="Light Mode",  # passt zum Start in Dark Mode
            command=self.toggle_dark_mode,
            font=("Arial", 12)
        )
        self.mode_button.pack(side="right")

        # Bereich für die Karte (Frage/Antwort)
        self.card_text = tk.Label(
            master,
            text="",
            wraplength=900,
            justify="center",
            font=("Arial", 24)
        )
        self.card_text.pack(expand=True)

        # Bottom-Frame für Navigationstasten
        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(fill="x", pady=10)

        self.prev_button = tk.Button(
            self.bottom_frame,
            text="←",
            font=("Arial", 14, "bold"),
            width=5,
            command=self.prev_card
        )
        self.prev_button.grid(row=0, column=0, padx=20)

        self.bottom_frame.grid_columnconfigure(1, weight=1)

        self.next_button = tk.Button(
            self.bottom_frame,
            text="→",
            font=("Arial", 14, "bold"),
            width=5,
            command=self.next_card
        )
        self.next_button.grid(row=0, column=2, padx=20)

        # Karten initial laden
        self.load_cards(self.selected_csv.get())
        self.index = 0
        self.showing_question = True

        # Dark Mode anwenden und erste Karte anzeigen
        self.apply_theme()
        self.display_card()

        # Bindings
        self.master.bind("<Button-1>", self.on_click)
        self.master.bind("<Left>", lambda e: self.prev_card())
        self.master.bind("<Right>", lambda e: self.next_card())
        self.master.bind("<space>", lambda e: self.toggle_flashcard())

    def load_cards(self, csv_file):
        """Lädt Karten aus der angegebenen CSV-Datei."""
        try:
            with open(csv_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.cards = [(row["Frage"], row["Antwort"]) for row in reader]
            if not self.cards:
                raise ValueError("Datei enthält keine Karten.")
            self.index = 0
            self.showing_question = True
        except Exception as e:
            messagebox.showerror("Fehler beim Laden", f"Kann die Datei '{csv_file}' nicht laden:\n{e}")
            self.cards = []
            self.index = 0
            self.showing_question = True

    def change_csv(self, selection):
        """Wird aufgerufen, wenn im Dropdown eine neue CSV ausgewählt wird."""
        self.load_cards(selection)
        self.display_card()

    def apply_theme(self):
        """Setzt Farben je nach aktuellem Modus."""
        if self.dark_mode:
            bg = self.dark_bg
            fg = self.dark_fg
            self.mode_button.config(text="Light Mode")
        else:
            bg = self.light_bg
            fg = self.light_fg
            self.mode_button.config(text="Dark Mode")

        self.master.configure(bg=bg)
        self.card_text.config(bg=bg, fg=fg)
        self.mode_button.master.config(bg=bg)
        self.mode_button.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)
        self.bottom_frame.config(bg=bg)
        self.prev_button.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)
        self.next_button.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)
        self.csv_menu.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)

    def display_card(self):
        """Zeigt aktuelle Frage oder Antwort an."""
        if not self.cards:
            self.card_text.config(text="Keine Karten geladen.")
            return

        frage, antwort = self.cards[self.index]
        text = frage if self.showing_question else antwort
        self.card_text.config(text=text)

    def on_click(self, event):
        widget = self.master.winfo_containing(event.x_root, event.y_root)

        # Klicks auf Dropdown-Menü und zugehöriges Menü ignorieren
        if widget == self.csv_menu or isinstance(widget, tk.Menu):
            return

        # Klicks auf Buttons ignorieren
        if widget in (self.mode_button, self.prev_button, self.next_button):
            return

        # Linksklick toggelt Frage/Antwort oder springt weiter
        if self.showing_question:
            self.showing_question = False
        else:
            self.next_card()
            return
        self.display_card()

    def toggle_flashcard(self):
        """Leertaste toggelt zwischen Frage und Antwort."""
        if not self.cards:
            return
        self.showing_question = not self.showing_question
        self.display_card()

    def prev_card(self):
        """Springt zur vorherigen Karte und zeigt Frage."""
        if not self.cards:
            return
        self.index = (self.index - 1) % len(self.cards)
        self.showing_question = True
        self.display_card()

    def next_card(self):
        """Springt zur nächsten Karte und zeigt Frage."""
        if not self.cards:
            return
        self.index = (self.index + 1) % len(self.cards)
        self.showing_question = True
        self.display_card()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
