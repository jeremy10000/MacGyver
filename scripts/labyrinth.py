#! /usr/bin/env python3
# coding: utf-8

"""
    Labyrinth :
    laod the file, laod the positions of the elements
    and randomly places items on the roads.
"""

from random import sample

from config import settings as st


class Labyrinth:
    """ Labyrinth file management. """
    def __init__(self):
        self.level_design = []
        self.roads = []
        self.walls = []
        self.items_list = []


    def load_file_and_position(self, filename, dico):
        """ Load the labyrinth file and memorizes the positions of the elements. """
        file = open(filename, "r")
        lines = file.readlines()
        for pos_y, item in enumerate(lines):
            for pos_x, char in enumerate(item):
                if char != "\n":
                    self.level_design.append(((pos_x, pos_y), item[pos_x].upper()))

                    for key in dico:
                        if item[pos_x] == dico[key][0]:
                            dico[key][2].append((pos_x, pos_y))
        file.close()


    def set_items(self):
        """ Randomly places items on the roads. """
        self.items_list = sample(self.roads, st.ITEMS)


    def add_roads(self, pos):
        """ Adds the starting position of the playable character to the roads. """
        self.roads.append(pos)
