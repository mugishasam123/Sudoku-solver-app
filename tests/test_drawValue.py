import unittest
from unittest.mock import MagicMock
from scripts.modules.board_drawing import draw_val


class TestDrawVal(unittest.TestCase):
    def setUp(self):
        self.font = MagicMock()
        self.screen = MagicMock()
        self.x = 0
        self.y = 0
        self.dif = 10

    def test_draw_val(self):
        val = 5
        draw_val(val, self.font, self.screen, self.x, self.y, self.dif)

        # Assert that the render method was called with the correct arguments
        self.font.render.assert_called_once_with(str(val), 1, (0, 0, 0))
        self.screen.blit.assert_called_once_with(self.font.render.return_value, (self.x * self.dif + 18, self.y * self.dif + 10))
