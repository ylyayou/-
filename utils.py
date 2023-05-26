import pygame
from settings import *


def debug(info, x, y):
    display_surface = pygame.display.get_surface()
    debug_surf = font_for_game.render(str(info), True, 'Black')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    display_surface.blit(debug_surf, debug_rect)