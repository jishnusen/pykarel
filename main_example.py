#!/usr/bin/env python3
import Karel

karel = Karel.Robot(10, 1, Karel.SOUTH, beepers=100)

world = Karel.World("worlds/11x11-maze.txt")
world.add_robot(karel)
world.set_speed(1)

karel.move()
karel.move()
karel.turnleft()
karel.move()
karel.move()
karel.move()
karel.turnright()
karel.move()
karel.move()
