Help MacGyver to escape !
===========================

Description
---------------------------------

It's a 2D game.
MacGyver's locked up, you need to collect three items to escape the labyrinth.

The game
-------------------------
* Only one level, the labyrinth file is setting on config/labyrinth.txt.
* MacGyver is controlled by the arrow keys on the keyboard.
* Items are randomly distributed in the labyrinth and change with each new game.
* The game window is a square of 15 squares.
* MacGyver retrieve an object simply by moving on it.
* MacGyver wins if he shows up in front of the guardian with all the items.

Requirements
------------
```
pip install -r requirements.txt
```

Virtual environment (Mac OS X)
------------------------------
```
pip install virtualenv
virtualenv -p python3 env
source env/bin/activate
```

Play
----  
```
python3 game.py
```

Standalone (CX_Freeze)
----  
```
python3 setup.py build
```

Tests
---------
* Mac OS X Sierra + python 3.7
* PEP 8 : All files 10/10 (Pylint)
