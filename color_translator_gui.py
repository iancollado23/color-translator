# color_translator_gui.py

import tkinter as tk
from tkinter import messagebox
import webcolors
import logging
from typing import Optional

# Configure logging
logging.basicConfig(filename='color_translator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ColorTranslatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Universal Color Translator")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # Configure grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)

        self.setup_ui()

    def setup_ui(self):
        """Sets up the UI components."""
        # Prompt Label
        prompt_label = tk.Label(self.root, text="Enter a color name:", font=("Helvetica", 12))
        prompt_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        # Entry Widget
        self.entry = tk.Entry(self.root, width=25, font=("Helvetica", 12))
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Translate Button
        translate_button = tk.Button(
            self.root,
            text="Translate",
            command=self.get_hex_code,
            font=("Helvetica", 12),
            bg="#4CAF50",
            fg="white"
        )
        translate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Color Swatch
        self.color_swatch = tk.Label(self.root, bg="white", width=20, height=2, relief="sunken", borderwidth=1)
        self.color_swatch.grid(row=3, column=0, columnspan=2, pady=10)

        # Copy Button
        copy_button = tk.Button(
            self.root,
            text="Copy Hex Code",
            command=self.copy_to_clipboard,
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white"
        )
        copy_button.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_color_to_hex(self, color_name: str) -> Optional[str]:
        """
        Translates a color name to its hexadecimal code.

        Args:
            color_name (str): The name of the color to translate.

        Returns:
            Optional[str]: The hexadecimal code of the color or None if not found.
        """
        try:
            return webcolors.name_to_hex(color_name.lower())
        except ValueError:
            return None

    def get_hex_code(self):
        """Retrieves the color name from the entry widget, translates it to hex,
        and updates the result label and color swatch accordingly.
        """
        color = self.entry.get().strip()
        if not color:
            messagebox.showwarning("Input Error", "Please enter a color name.")
            logging.warning("User tried to translate an empty input.")
            return
        
        hex_code = self.translate_color_to_hex(color)
        if hex_code:
            self.result_label.config(
                text=f"The hexadecimal code for '{color.title()}' is {hex_code}",
                fg="green"
            )
            self.color_swatch.config(bg=hex_code)
            logging.info(f"Translated color '{color}' to hex code '{hex_code}'.")
        else:
            self.result_label.config(text="Color not found. Please try another color.", fg="red")
            self.color_swatch.config(bg="white")
            logging.error(f"Color '{color}' not found.")

    def copy_to_clipboard(self):
        """Copies the current hex code displayed to the clipboard."""
        hex_code = self.result_label.cget("text").split()[-1]
        if hex_code.startswith("#"):
            self.root.clipboard_clear()
            self.root.clipboard_append(hex_code)
            messagebox.showinfo("Copied", f"Hex code {hex_code} copied to clipboard.")
            logging.info(f"Copied hex code '{hex_code}' to clipboard.")
        else:
            messagebox.showwarning("Copy Error", "No valid hex code to copy.")
            logging.warning("User attempted to copy an invalid hex code.")

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = ColorTranslatorApp(root)
    root.mainloop()
