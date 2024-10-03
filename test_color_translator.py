# test_color_translator.py

import unittest
from color_translator import translate_color_to_hex

class TestColorTranslator(unittest.TestCase):
    
    def test_known_colors(self):
        self.assertEqual(translate_color_to_hex("red"), "#FF0000")
        self.assertEqual(translate_color_to_hex("blue"), "#0000FF")
        self.assertEqual(translate_color_to_hex("green"), "#008000")
        self.assertEqual(translate_color_to_hex("yellow"), "#FFFF00")
        self.assertEqual(translate_color_to_hex("black"), "#000000")
        self.assertEqual(translate_color_to_hex("white"), "#FFFFFF")
        self.assertEqual(translate_color_to_hex("orange"), "#FFA500")
        self.assertEqual(translate_color_to_hex("purple"), "#800080")
        self.assertEqual(translate_color_to_hex("pink"), "#FFC0CB")
        self.assertEqual(translate_color_to_hex("cyan"), "#00FFFF")
        self.assertEqual(translate_color_to_hex("magenta"), "#FF00FF")
        self.assertEqual(translate_color_to_hex("lime"), "#00FF00")
        self.assertEqual(translate_color_to_hex("maroon"), "#800000")
        self.assertEqual(translate_color_to_hex("navy"), "#000080")
        self.assertEqual(translate_color_to_hex("olive"), "#808000")
        self.assertEqual(translate_color_to_hex("teal"), "#008080")
        self.assertEqual(translate_color_to_hex("silver"), "#C0C0C0")
        self.assertEqual(translate_color_to_hex("gray"), "#808080")
        self.assertEqual(translate_color_to_hex("brown"), "#A52A2A")
        self.assertEqual(translate_color_to_hex("coral"), "#FF7F50")
    
    def test_case_insensitivity(self):
        self.assertEqual(translate_color_to_hex("Red"), "#FF0000")
        self.assertEqual(translate_color_to_hex("BLUE"), "#0000FF")
        self.assertEqual(translate_color_to_hex("Green"), "#008000")
        self.assertEqual(translate_color_to_hex("YELLOW"), "#FFFF00")
    
    def test_unknown_color(self):
        self.assertEqual(translate_color_to_hex("unknowncolor"), "Color not found")
        self.assertEqual(translate_color_to_hex(""), "Color not found")
        self.assertEqual(translate_color_to_hex("123"), "Color not found")

if __name__ == "__main__":
    unittest.main()
