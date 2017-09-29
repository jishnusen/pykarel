#!/usr/bin/env python3
import Karel

def turnright():
	karel.turnleft()
	karel.turnleft()
	karel.turnleft()

karel = Karel.Robot(1, 0, Karel.SOUTH, beepers=100)

world = Karel.World("worlds/10x20-room.txt")
world.add_robot(karel)
world.set_speed(1)

karel.move()
karel.move()
karel.turnleft()
karel.move()
karel.move()
karel.move()
turnright()
karel.move()
karel.move()
