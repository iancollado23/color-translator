# color_translator_gui.py

import tkinter as tk
from tkinter import messagebox

def translate_color_to_hex(color_name):
    # Expanded color mapping
    color_map = {
        "red": "#FF0000",
        "blue": "#0000FF",
        "green": "#008000",
        "yellow": "#FFFF00",
        "black": "#000000",
        "white": "#FFFFFF",
        "orange": "#FFA500",
        "purple": "#800080",
        "pink": "#FFC0CB",
        "cyan": "#00FFFF",
        "magenta": "#FF00FF",
        "lime": "#00FF00",
        "maroon": "#800000",
        "navy": "#000080",
        "olive": "#808000",
        "teal": "#008080",
        "silver": "#C0C0C0",
        "gray": "#808080",
        "brown": "#A52A2A",
        "coral": "#FF7F50"
    }
    
    # Convert input to lowercase to make it case-insensitive
    color_name = color_name.lower()
    
    # Return the hex code or a default message if not found
    return color_map.get(color_name, "Color not found")

def get_hex_code():
    color = entry.get().strip()
    if not color:
        messagebox.showwarning("Input Error", "Please enter a color name.")
        return
    hex_code = translate_color_to_hex(color)
    if hex_code == "Color not found":
        result_label.config(text=hex_code, fg="red")
    else:
        result_label.config(text=f"The hexadecimal code for {color} is {hex_code}", fg="green")

# Create the main window
root = tk.Tk()
root.title("Universal Color Translator")
root.geometry("400x200")
root.resizable(False, False)

# Create and place widgets
prompt_label = tk.Label(root, text="Enter a color name:", font=("Arial", 12))
prompt_label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=get_hex_code, font=("Arial", 12))
translate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
