import pygame
from config import FONT_NAME, FONT_SIZE

def init_display(width, height, title):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen

def init_font():
    return pygame.font.SysFont(FONT_NAME, FONT_SIZE)