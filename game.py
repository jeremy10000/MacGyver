#! /usr/bin/env python3
# coding: utf-8

import sys

import pygame

from config import settings as st
from scripts import gameview as gv
from scripts import characters as ch
from scripts import labyrinth as lb

"""
    game.py : Launch the game.
"""


class Play:
    """ Game management.
        Main class - she will interact with the other classes. """
    def __init__(self, hero, enemy, labyrinth, view):
        """ Initialize """
        # Is the game running ?
        self.play = True

        self.hero = hero
        self.enemy = enemy
        self.laby = labyrinth
        self.view = view

        # All visible objects of the game.
        self.elements = {
            "MACGYVER": [st.MACGYVER,
                         pygame.image.load(st.MACGYVER_IMAGE),
                         self.hero.position],
            "ENEMY": [st.ENEMY,
                      pygame.image.load(st.ENEMY_IMAGE),
                      self.enemy.position],
            "ROADS": [st.ROADS,
                      pygame.image.load(st.ROAD_IMAGE),
                      self.laby.roads],
            "WALLS": [st.WALLS,
                      pygame.image.load(st.WALL_IMAGE),
                      self.laby.walls]
        }

        # Items to collect.
        self.items = [
            pygame.image.load(st.TUBE_IMAGE),
            pygame.image.load(st.NEEDLE_IMAGE),
            pygame.image.load(st.ETHER_IMAGE)
        ]

        # Calls methods from other classes.
        self.laby.load_file_and_position(st.LABYRINTH_FILE, self.elements)
        self.hero.move(self.elements["MACGYVER"][2])
        self.enemy.move(self.elements["ENEMY"][2])
        self.view.title(self.hero.items, st.ITEMS)
        self.view.show_sprite(self.laby.level_design, self.elements)
        self.laby.set_items()
        self.laby.add_roads(self.hero.position)
        self.view.show_items(self.laby.items_list, st.ITEMS, self.items)

        pygame.display.update()

    def events(self):
        """ Waiting for an event. """
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self._event_quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.play is True:
                        self._check(self.hero.posx, self.hero.posy-1)

                    if event.key == pygame.K_DOWN and self.play is True:
                        self._check(self.hero.posx, self.hero.posy+1)

                    if event.key == pygame.K_RIGHT and self.play is True:
                        self._check(self.hero.posx+1, self.hero.posy)

                    if event.key == pygame.K_LEFT and self.play is True:
                        self._check(self.hero.posx-1, self.hero.posy)

                    if event.key == pygame.K_y and self.play is False:
                        return False

                    if event.key == pygame.K_n and self.play is False:
                        self._event_quit()

    def _check(self, pos_x, pos_y):
        """ Check to see if it's valid. """
        is_inside = self._inside(pos_x, pos_y)

        if is_inside is True:
            if (pos_x, pos_y) in self.laby.items_list:
                self._moving(pos_x, pos_y,
                             self.hero.posx,
                             self.hero.posy)
                self.hero.move((pos_x, pos_y))
                self.laby.items_list.remove((pos_x, pos_y))
                self.hero.items_collected()
                self.view.title(self.hero.items, st.ITEMS)

            elif (pos_x, pos_y) in self.laby.roads:
                self._moving(pos_x, pos_y,
                             self.hero.posx,
                             self.hero.posy)
                self.hero.move((pos_x, pos_y))

            elif (pos_x, pos_y) == self.enemy.position:
                self._moving(pos_x, pos_y,
                             self.hero.posx,
                             self.hero.posy)
                self.hero.move((pos_x, pos_y))
                self.endgame()

            pygame.display.update()

    def _inside(self, pos_x, pos_y):
        """ Is it in the square ? """
        square = list(range(0, 15))
        if ((pos_x in square) and (pos_y in square)):
            return True
        return False

    def _moving(self, new_pos_x, new_pos_y, pos_x, pos_y):
        """ Update positions. """
        pos_hero = ((new_pos_x * st.SPRITE_SIZE),
                    ((new_pos_y * st.SPRITE_SIZE)))
        pos_road = ((pos_x * st.SPRITE_SIZE), ((pos_y * st.SPRITE_SIZE)))

        self.view.refresh(pos_hero, pos_road, self.elements)

    def endgame(self):
        """ End of the game. """
        if self.hero.items == st.ITEMS:
            self.view.message("You Win !", 6, 7)
            self.view.message("Press (y) to play again or (n) to quit", 2, 8)
        else:
            self.view.message("You Lose !", 6, 7)
            self.view.message("Press (y) to play again or (n) to quit", 2, 8)

        self.play = False
        pygame.display.update()

    def _event_quit(self):
        """ Close the game. """
        pygame.quit()
        sys.exit()


def main():
    """ Launch the game. """
    while True:

        macgyver = ch.Character()
        enemy = ch.Character()
        laby = lb.Labyrinth()
        view = gv.GameView()

        play = Play(macgyver, enemy, laby, view)
        play.events()

        del macgyver, enemy, laby, view, play


if __name__ == "__main__":
    main()
