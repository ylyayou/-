import pygame
import os
pygame.init()

opts = {
    "alias": ('кот', 'котик', 'кошка', 'котенок', 'кошечка', 'кит',
              'усатый',),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "ocenka": ('какую нам поставят оценку', 'оцени нашу курсовую работу',),
        "stupid1": ('кто самая лучшая староста', 'кто самая красивая староста', 'кто самая классная староста'),

    }
}


FPS = 60
WIDTH = 1280
HEIGHT = 720
FONT_SIZE = int((WIDTH+HEIGHT)/75)


font_for_game = pygame.font.Font(os.path.join("fonts", 'arial_bolditalicmt.ttf'), FONT_SIZE)