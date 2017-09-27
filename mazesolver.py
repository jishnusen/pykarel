#!/usr/bin/env python3
import Karel

def turnright():
	karel.turnleft()
	karel.turnleft()
	karel.turnleft()

world = Karel.World("worlds/11x11-maze.txt")
#~ world = Karel.World("worlds/39x39-maze.txt")
mazestart = {'x':world.grid[0].index(' '), 'y':0}
mazeend = {'x':world.grid[-1].index(' '), 'y':len(world.grid)-1}
karel = Karel.Robot(mazestart['x'], mazestart['y'], Karel.SOUTH, beepers=100)
world.add_robot(karel)
world.set_speed(3)

while karel.y != mazeend['y'] or karel.x != mazeend['x']:
	# check free space right, straight, left, or turn around
	turnright()
	while True:
		if karel.front_is_clear():
			break
		karel.turnleft()
	karel.move()
