#! /usr/bin/env python3
# coding: utf-8

import pygame

from config import settings as st

"""
    PyGame window :
    title, size and sprites.
"""


class GameView:
    """ PyGame window management. """
    def __init__(self):
        """ Initialize """
        pygame.init()
        self.screen = pygame.display.set_mode((st.SCREEN_SIZE, st.SCREEN_SIZE))
        self.screen_title = pygame.display.set_caption("MacGyver")

    def show_sprite(self, labyrinth, sprites):
        """ Place the images in the window. """
        for i in labyrinth:
            pos_x = i[0][0] * st.SPRITE_SIZE
            pos_y = i[0][1] * st.SPRITE_SIZE
            for key in sprites:
                if key == "MACGYVER" and i[1] == sprites[key][0]:
                    self.screen.blit(sprites["ROADS"][1].convert(),
                                     (pos_x, pos_y))
                    self.screen.blit(sprites[key][1].convert_alpha(),
                                     (pos_x, pos_y))

                elif i[1] == sprites[key][0]:
                    self.screen.blit(sprites[key][1].convert(),
                                     (pos_x, pos_y))

    def show_items(self, nb_items, max_items, items_list):
        """ Place items on the roads. """
        num = 0
        while num != max_items:
            self.screen.blit(items_list[num].convert_alpha(),
                             ((nb_items[num][0] * st.SPRITE_SIZE),
                              (nb_items[num][1] * st.SPRITE_SIZE)))
            num += 1

    def title(self, nb_items, max_items):
        """ Change the title. """
        self.screen_title = pygame.display.set_caption(
            "MacGyver - Items collected ({}/{})".format(nb_items, max_items))

    def refresh(self, pos_hero, pos_road, sprites):
        """ Update the window. """
        self.screen.blit(sprites["MACGYVER"][1], pos_hero)
        self.screen.blit(sprites["ROADS"][1], pos_road)

    def message(self, text, pos_x, pos_y):
        """ Show a message. """
        font = pygame.font.Font(None, st.SPRITE_SIZE)
        bg_color = (255, 255, 255)
        font_color = (0, 0, 0)
        message = font.render(text, True, bg_color, font_color)
        self.screen.blit(message,
                         (st.SPRITE_SIZE * pos_x, st.SPRITE_SIZE * pos_y))
