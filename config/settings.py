#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

""" Variables """


# Localisation
BASE_DIR = Path(__file__).resolve().parent.parent
MACGYVER_IMAGE = str(BASE_DIR / "images" / "MacGyver.png")
ENEMY_IMAGE = str(BASE_DIR / "images" / "Enemy.png")
WALL_IMAGE = str(BASE_DIR / "images" / "structures.png")
ROAD_IMAGE = str(BASE_DIR / "images" / "road.png")
TUBE_IMAGE = str(BASE_DIR / "images" / "tube_plastique.png")
NEEDLE_IMAGE = str(BASE_DIR / "images" / "aiguille.png")
ETHER_IMAGE = str(BASE_DIR / "images" / "ether.png")

# Labyrinth
LABYRINTH_FILE = str(BASE_DIR / "config" / "labyrinth.txt")
SPRITE_SIZE = 30
MACGYVER = "M"
ENEMY = "G"
WALLS = "W"
ROADS = " "
ITEMS = 3

# Pygame window
SCREEN_SIZE = 15 * SPRITE_SIZE
