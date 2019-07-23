#! /usr/bin/env python3
# coding: utf-8

"""
    Character :
    position, number of items and the ability to move.
"""


class Character:
    """ Character management. """
    def __init__(self):
        """ Initialize """
        self.position = (0, 0)
        self.items = 0

    def items_collected(self):
        """ Item found. """
        self.items += 1

    def move(self, new_pos):
        """ Change the position. """
        self.position = new_pos
        self.posx = new_pos[0]
        self.posy = new_pos[1]
