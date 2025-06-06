Title: CSV Flashcards App

Overview:
This is a simple flashcard application written in Python using the Tkinter GUI toolkit. It works with any CSV file that has two columns (Frage, Antwort). You can store multiple CSV files in the same folder, choose among them via a dropdown menu, toggle between question and answer with the spacebar or mouse click, and navigate forward/backward through cards with arrow keys or on-screen buttons. A Windows executable (.exe) is provided so Windows users can run the app without installing Python.

Contents of this repository:

flashcard_app.py: The main Python script for the flashcard application.

deck_full.csv (example): A sample deck with full-length questions and answers.

deck_short.csv (example): A sample deck with concise prompts and answers.

csv-flashcards.exe: A PyInstaller-generated Windows executable of the app.

Additional .csv files can be added here and will automatically appear in the app’s dropdown menu.

Prerequisites:

If you plan to run the Python version (flashcard_app.py), you need Python 3.6 or newer installed.

The app relies only on standard Python libraries: tkinter, csv, and os. No extra pip packages are required.

If your system does not have Tkinter, install it:

On Ubuntu/Debian: sudo apt-get install python3-tk

On Windows/Mac, Tkinter is usually bundled with Python. If missing, reinstall Python and ensure you include the “tk/tcl” option.

Installation and Setup:

Clone or download this repository to your local machine.

If you are on Windows and prefer not to install Python, simply double-click csv-flashcards.exe to run the app.

If you want to run the Python script directly:
a. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux).
b. Navigate to the folder containing flashcard_app.py and the CSV files.
c. Run: python flashcard_app.py

Ensure that any custom CSV files you create follow the two-column format with headers “Frage” and “Antwort” (German for “Question” and “Answer”). Place them in the same folder as flashcard_app.py. They will appear in the dropdown automatically.

CSV File Format:
Each CSV file must have exactly two columns and include a header row. Example structure:
Frage,Antwort
What is the capital of France?,Paris
Define polymorphism in OOP.,Polymorphism allows objects of different classes to be treated as instances of a common base class.

You can create as many decks as you like—each new CSV will show up in the app’s dropdown list.

How to Use the App:

Launch the application (double-click the .exe on Windows or run flashcard_app.py in Python).

In the top-left corner, use the dropdown menu to select which CSV deck you want to study.

Toggle dark/light mode by clicking the button in the top-right.

To reveal an answer or go back to the question for the current card, press the spacebar or click anywhere in the blank area of the window (outside of buttons and menus). Each press toggles between showing the question and the answer.

To move to the next card, press the right-arrow key or click the “→” button at the bottom. To go to the previous card, press the left-arrow key or click the “←” button. After moving, the question side will be shown by default.

If you are browsing the CSV dropdown menu or clicking on any button (e.g., dark mode toggle, navigation buttons), those clicks will not flip the card.

Creating Your Own Flashcard Decks:

Copy one of the example CSV files (for instance, deck_short.csv) and rename it, for example, “my_deck.csv.”

Open the file in a spreadsheet editor or text editor.

Replace the questions and answers with your own content, keeping the two-column format and header labels “Frage” and “Antwort.”

Save the file. When you launch the app, your new deck appears in the dropdown menu automatically.

Windows Executable (.exe):
For Windows users who do not have Python installed, you can run the application directly from the csv-flashcards.exe file included in this repository. Simply double-click the executable to launch the flashcard app. The .exe is created using PyInstaller and bundles Python and all dependencies into a single file.

Contributing and Customization:

Feel free to add, modify, or remove features. The code is commented to help you understand how it works.

You can add new CSV files (any name ending in .csv) to expand your decks. No changes to code are necessary.

If you’d like to implement advanced features—such as exporting to PDF or integrating spaced-repetition statistics—fork the repository, make your changes, and submit a pull request.

License:
This project is provided under the MIT License. You are free to use, modify, and redistribute it in any form, provided that the original license notice is included.
