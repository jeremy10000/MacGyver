#! /usr/bin/env python3
# coding: utf-8

"""
    Character :
    position, number of items and the ability to move.
"""

class Character:
    """ Character management. """
    def __init__(self):
        self.position = []
        self.items = 0


    def items_collected(self):
        """ Item found. """
        self.items += 1


    def move(self, new_pos):
        """ Change the position. """
        self.position[0] = new_pos


    @property
    def get_pos_x(self):
        """ Return the x position. """
        return self.position[0][0]


    @property
    def get_pos_y(self):
        """ Return the y position. """
        return self.position[0][1]
