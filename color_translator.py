# color_translator.py

def translate_color_to_hex(color_name):
    # Predefined color mapping
    color_map = {
        "red": "#FF0000",
        "blue": "#0000FF",
        "green": "#008000",
        "yellow": "#FFFF00",
        "black": "#000000",
        "white": "#FFFFFF",
        "orange": "#FFA500",
        "purple": "#800080"
    }
    
    # Convert input to lowercase to make it case-insensitive
    color_name = color_name.lower()
    
    # Return the hex code or a default message if not found
    return color_map.get(color_name, "Color not found")

if __name__ == "__main__":
    # Prompt user for input
    color = input("Enter a color name: ")
    # Get and print the corresponding hex code
    hex_code = translate_color_to_hex(color)
    print(f"The hexadecimal code for {color} is {hex_code}")
