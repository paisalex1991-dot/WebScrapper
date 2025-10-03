#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  return

import tkinter as tk
from tkinter import filedialog, messagebox
import re

# Global variable to store the selected file path
selected_file = None

def import_file():
    """Let the user select a file and store its path."""
    global selected_file
    selected_file = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if selected_file:
        messagebox.showinfo("File Imported", f"Selected file:\n{selected_file}")

def show_results():
    """Process the imported file with regex and show results."""
    global selected_file
    if not selected_file:
        messagebox.showwarning("No File", "Please import a file first!")
        return

    try:
        with open(selected_file, "r", encoding="utf-8") as f:
            text = f.read()

        # Regex to extract words
        words = re.findall(r'</td><td>(.*?)</td><td>', text)
        word_count = len(words)

        # Count frequency of each word
        freq = Counter(words)

        # Clear previous results
        result_box.delete("1.0", tk.END)

        # Insert results
        result_box.insert(tk.END, f"Total words: {word_count}\n\n")
        result_box.insert(tk.END, "Word Frequencies:\n")
        for word, count in freq.most_common():  # most_common() sorts by frequency
            result_box.insert(tk.END, f"{word}: {count}\n")

    except Exception as e:
        messagebox.showerror("Error", f"Could not read file:\n{e}")

def main():
    
    global result_box
    root = tk.Tk()
    root.title("Regex File Processor")
    root.geometry("300x400")

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    button1 = tk.Button(button_frame, text="Import", command=import_file, bg="blue", fg="white")
    button2 = tk.Button(button_frame, text="Results", command=show_results, bg="blue", fg="white")

    button1.pack(side="left", padx=10)
    button2.pack(side="left", padx=10)

    # Frame for results with scrollbar
    result_frame = tk.Frame(root)
    result_frame.pack(pady=20)

    # Scrollbar
    scrollbar = tk.Scrollbar(result_frame)
    scrollbar.pack(side="right", fill="y")

    # Result box (Text widget)
    result_box = tk.Text(result_frame, width=35, height=12, yscrollcommand=scrollbar.set)
    result_box.pack(side="left")
    scrollbar.config(command=result_box.yview)

    root.mainloop()
    
if __name__ == '__main__':
  main()
