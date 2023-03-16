import unittest
import pygame
from scripts.modules.board_drawing import draw

class TestDrawSudoku(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((500, 500))
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", 40)
        self.dif = self.screen.get_width() / 9
    
    def tearDown(self):
        pygame.quit()
        
    def test_draw(self):
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        draw(pygame, self.screen, self.dif, self.font, grid)
        self.assertEqual(pygame.surfarray.array2d(self.screen).shape, (500, 500))

if __name__ == '__main__':
    unittest.main()