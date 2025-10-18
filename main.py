import pygame, sys
from config import *
from utils import init_display, init_font
from textpath import draw_text_along_path

pygame.init()

screen = init_display(WIDTH, HEIGHT, WINDOW_TITLE)
font = init_font()

running = True
drawing = False
points = []

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                points = [event.pos]

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            points.append(event.pos)

    if len(points) > 1:
        pygame.draw.lines(screen, (0, 0, 0), False, points, 2)

    draw_text_along_path(screen, TEXT_STRING, points, font, TEXT_COLOR)

    pygame.display.flip()