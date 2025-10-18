import math
import pygame

def draw_text_along_path(surface, text, path, font, color):
    """Draw text characters along a path (list of points)."""
    if len(path) < 2:
        return

    text_index = 0
    dist_accum = 0
    char_spacing = font.size("A")[0] * 0.7

    for i in range(1, len(path)):
        (x1, y1), (x2, y2) = path[i - 1], path[i]
        dx, dy = x2 - x1, y2 - y1
        seg_length = math.hypot(dx, dy)

        while dist_accum + seg_length >= char_spacing:
            ratio = (char_spacing - dist_accum) / seg_length
            cx = x1 + dx * ratio
            cy = y1 + dy * ratio
            angle = math.degrees(math.atan2(dy, dx))

            char = text[text_index % len(text)]
            char_surf = font.render(char, True, color)
            char_surf = pygame.transform.rotate(char_surf, -angle)
            rect = char_surf.get_rect(center=(cx, cy))
            surface.blit(char_surf, rect)

            text_index += 1
            dist_accum -= char_spacing

        dist_accum += seg_length