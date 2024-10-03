# tests/test_color_translator.py

import unittest
from src.color_translator import translate_color_to_hex, load_color_map

class TestColorTranslator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.color_map = load_color_map('data/colors.json')

    def test_known_colors(self):
        test_cases = {
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
        for color, hex_code in test_cases.items():
            with self.subTest(color=color):
                self.assertEqual(translate_color_to_hex(color, self.color_map), hex_code)

    def test_case_insensitivity(self):
        test_cases = {
            "Red": "#FF0000",
            "BLUE": "#0000FF",
            "Green": "#008000",
            "YeLLoW": "#FFFF00",
            "Black": "#000000",
            "WHITE": "#FFFFFF"
        }
        for color, hex_code in test_cases.items():
            with self.subTest(color=color):
                self.assertEqual(translate_color_to_hex(color, self.color_map), hex_code)

    def test_unknown_color(self):
        test_cases = ["unknowncolor", "bluish", "123", "!@#$", "magentaa"]
        for color in test_cases:
            with self.subTest(color=color):
                self.assertEqual(translate_color_to_hex(color, self.color_map), "Color not found")

    def test_empty_input(self):
        self.assertEqual(translate_color_to_hex("", self.color_map), "Input cannot be empty.")

if __name__ == "__main__":
    unittest.main()
