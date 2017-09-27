# PyKarel

A Python educational programming language based on Karel

https://en.wikipedia.org/wiki/Karel_(programming_language)

## Resources

* [Introduction](https://github.com/cpiehl/pykarel#introduction)
* [Getting Started](https://github.com/cpiehl/pykarel#getting-started)
* [Wiki](https://github.com/cpiehl/pykarel/wiki)
* [API Reference](https://github.com/cpiehl/pykarel/wiki/API-Reference)
* [Examples](https://github.com/cpiehl/pykarel/wiki/Examples)

## Installation

1. Download and install Python 3 from the official website https://www.python.org/downloads/
2. Extract the latest release of PyKarel https://github.com/cpiehl/pykarel/releases/latest

## Introduction

Karel is a triangular robot that lives in a 2-dimensional grid world like this:
```
######################
#                    #
#                    #
#                    #
#                    #
#                    #
#                    #
#                    #
#     ▲              #
#                    #
#                    #
######################
```
In the world there are round objects called Beepers.  Karel can pick these up to move them around.
```
#######
#     #
# ► o #
#     #
#######
```
Karel has 4 basic commands to interact with the world:
```python
move() # moves forward one space
turnleft() # turns 90 degrees left
pick_beeper() # picks up a beeper and puts it in Karel's beeper storage
put_beeper() # puts down a beeper from Karel's beeper storage
```
In order to safely interact with the world, Karel also has 2 commands to learn about its surroundings:
```python
front_is_clear() # checks if Karel can safely move forward
check_beeper() # checks if a beeper is in front of Karel
```

## Getting Started

Every PyKarel program must start with
```python
import Karel
```
Create a Karel robot at coordinates X=1, Y=1, facing South
```python
import Karel
karel = Karel.Robot(1, 1, Karel.SOUTH)
```
Create a World by loading a World file and add karel to it
```python
import Karel
karel = Karel.Robot(1, 1, Karel.SOUTH)
world = Karel.World("worlds/10x20-room-closed.txt")
world.add_robot(karel)
```
Move Karel forward one space, turn left 90 degrees, then move forward again
```python
import Karel
karel = Karel.Robot(1, 1, Karel.SOUTH)
world = Karel.World("worlds/10x20-room-closed.txt")
world.add_robot(karel)

karel.move()
karel.turnleft()
karel.move()
```
But be careful! Karel could become damaged if it rams into a wall at full speed! It is a good idea to check if it can safely move first.
```python
if karel.front_is_clear():
  karel.move()
karel.turnleft()
if karel.front_is_clear():
  karel.move()
```
Lastly, Karel is programmable to accept more complex commands!  A common addition is telling Karel how to turn right:
```python
import Karel

def turnright():
  karel.turnleft()
  karel.turnleft()
  karel.turnleft()
  
karel = Karel.Robot(1, 1, Karel.SOUTH)
world = Karel.World("worlds/10x20-room-closed.txt")
world.add_robot(karel)

if karel.front_is_clear():
  karel.move()
karel.turnleft()
if karel.front_is_clear():
  karel.move()
turnright()
if karel.front_is_clear():
  karel.move()
```
