import unittest
import pygame
from scripts.modules.board_drawing import draw, draw_box
from scripts.modules.check_valid import valid
from scripts.modules.auto_solve import solve

class TestSolve(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.font = pygame.font.SysFont(None, 40)
        self.dif = 500/9
        self.grid =[
               [7, 8, 0, 4, 0, 0, 1, 2, 0],
               [6, 0, 0, 0, 7, 5, 0, 0, 9],
               [0, 0, 0, 6, 0, 1, 0, 7, 8],
               [0, 0, 7, 0, 4, 0, 2, 6, 0],
               [0, 0, 1, 0, 5, 0, 9, 3, 0],
               [9, 0, 4, 0, 6, 0, 0, 0, 5],
               [0, 7, 0, 3, 0, 0, 0, 1, 2],
               [1, 2, 0, 0, 0, 7, 4, 0, 0],
               [0, 4, 9, 2, 0, 6, 0, 0, 7]
            ]
        
    def test_solve(self):
        solved = solve(self.grid, 0, 0, pygame, self.screen, draw, self.font, self.dif, draw_box, valid)
        self.assertTrue(solved)
            
    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
