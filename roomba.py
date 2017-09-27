#!/usr/bin/env python3
import Karel

def turnright():
	karel.turnleft()
	karel.turnleft()
	karel.turnleft()

def scoop():
	if karel.check_beeper():
		karel.pick_beeper()
	karel.move()

karel = Karel.Robot(1, 0, Karel.SOUTH)
world = Karel.World("worlds/11x20-roomba.txt")
#~ karel = Karel.Robot(8, 0, Karel.SOUTH)
#~ world = Karel.World("worlds/11x20-roomba-hard.txt")
world.add_robot(karel)
world.set_speed(3)

x_dist = 0
# clean room
while karel.front_is_clear():
	scoop()
	karel.turnleft()
	# move across
	while karel.front_is_clear():
		scoop()
		x_dist += 1
	# go down one row
	turnright()
	if karel.front_is_clear():
		scoop()
	turnright()
	# move back
	while karel.front_is_clear():
		scoop()
		x_dist -= 1
	karel.turnleft()

# go home, for funsies
while karel.dir != Karel.WEST:
	karel.turnleft()
while karel.front_is_clear():
	karel.move()
	x_dist -= 1
while karel.dir != Karel.NORTH:
	karel.turnleft()
while karel.front_is_clear():
	karel.move()
if x_dist != 0:
	turnright()
	while karel.front_is_clear() and x_dist != 0:
		scoop()
		x_dist += 1
	karel.turnleft()
	karel.move()
karel.turnleft()
karel.turnleft()
