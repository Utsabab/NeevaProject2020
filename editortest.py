from editor import ImprovedEditor
import unittest


class ImprovedEditorTest(unittest.TestCase):
    def test_print_cutpaste(self):
        s = ImprovedEditor("Hello friend")
        s.cut(5,7)
        result = s.paste(3)
        expected = "Hel floriend"
        self.assertEqual(result, expected)

    def test_print_copypastepaste(self):
        s = ImprovedEditor("Hello friend")
        s.copy(5, 7)
        s.paste(12)
        result = s.paste(9)
        expected = "Hello fri fend f"
        self.assertEqual(result, expected)

    def test_print_gettext(self):
        s = ImprovedEditor("Hello friend")
        result = s.get_text()
        expected = "Hello friend"
        self.assertEqual(result, expected)

    def test_print_misspellings(self):
        s = ImprovedEditor("sports yyxz metro")
        result = s.misspellings()
        expected = 1
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()