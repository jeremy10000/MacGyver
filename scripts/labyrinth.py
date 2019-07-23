#! /usr/bin/env python3
# coding: utf-8

from random import sample

from config import settings as st

"""
    Labyrinth :
    laod the file, laod the positions of the elements
    and randomly places items on the roads.
"""


class Labyrinth:
    """ Labyrinth file management. """
    def __init__(self):
        """ Initialize """
        self.level_design = []
        self.roads = []
        self.walls = []
        self.items_list = []

    def load_file_and_position(self, filename, dictio):
        """ Load the labyrinth file
        and memorizes the positions of the elements. """
        file = open(filename, "r")
        lines = file.readlines()
        for pos_y, item in enumerate(lines):
            for pos_x, char in enumerate(item):
                if char != "\n":
                    self.level_design.append(
                                            ((pos_x, pos_y),
                                             char.upper()))

                    for key in dictio:
                        if key == "MACGYVER" and char == dictio[key][0]:
                            dictio[key][2] = (pos_x, pos_y)

                        elif key == "ENEMY" and char == dictio[key][0]:
                            dictio[key][2] = (pos_x, pos_y)

                        elif char == dictio[key][0]:
                            dictio[key][2].append((pos_x, pos_y))
        file.close()

    def set_items(self):
        """ Randomly places items on the roads. """
        self.items_list = sample(self.roads, st.ITEMS)

    def add_roads(self, pos):
        """ Adds the starting position of the playable character
        to the roads. """
        self.roads.append(pos)
