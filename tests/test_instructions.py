import unittest
from unittest.mock import MagicMock
from scripts.modules.instructions import instruction

class TestStringMethods(unittest.TestCase):

    def test_instruction(self):
        # Mock the screen and font arguments
        screen = MagicMock()
        font = MagicMock()
        instruction(screen, font)
        # Assert that the blit method was called  on the screen object
        screen.blit.assert_called_with(font.render.return_value, (20, 540))
        # Assert that the render method was called  on the font object
        font.render.assert_called_with("PRESS 'ENTER' TO AUTO-SOLVE | PRESS 'D' TO RESET THE BOARD", 1, (0, 0, 0))

if __name__ == '__main__':
    unittest.main()