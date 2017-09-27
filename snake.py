# Hacked together Snake implementation using Karels as the tail
# Uses boring algorithm, needs a proper AI
import Karel
import random

def move_snake(dir):
	x = world.robots[0].x + Karel.Robot.moves[dir][0]
	y = world.robots[0].y + Karel.Robot.moves[dir][1]

	world.robots[-1].x = x
	world.robots[-1].y = y
	world.robots[-1].dir = dir
	world.robots = world.robots[-1:] + world.robots[:-1]

def eat(x, y, dir):
	karel.pick_beeper()
	world.add_robot(Karel.Robot(x, y, dir))
	world.robots = world.robots[-1:] + world.robots[:-1]
	if len(world.robots) >= (world.height - 2) * (world.width - 2):
		return -1, -1
	return new_beeper()

def new_beeper():
	(x, y) = (world.robots[0].x, world.robots[0].y)
	while (x, y) in [(r.x, r.y) for r in world.robots]:
		x = random.randint(1, world.width - 2)
		y = random.randint(1, world.height - 2)
	world.grid[y][x] = 'o'
	return x, y

world = Karel.World("worlds/10x20-room-closed.txt")
world.add_robot(Karel.Robot(1, 1, Karel.EAST))
world.set_speed(3)

(x, y) = new_beeper()

while True:
	karel = world.robots[0]

	# Boring non-AI pathing algorithm
	if karel.y == 1:
		if karel.x == 20:
			karel.dir = Karel.SOUTH
		else:
			karel.dir = Karel.EAST
	elif karel.y == 10:
		if karel.x % 2 == 0:
			karel.dir = Karel.WEST
		else:
			karel.dir = Karel.NORTH
	elif karel.y == 2 and karel.x != 1:
		if karel.dir == Karel.NORTH:
			karel.dir = Karel.WEST
		elif karel.dir == Karel.WEST:
			karel.dir = Karel.SOUTH

	if karel.front_is_clear():
		if karel.check_beeper():
			(x, y) = eat(x, y, karel.dir)
		else:
			move_snake(karel.dir)

		world.print_world()
	else:
		break
