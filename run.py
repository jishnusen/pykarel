#!/usr/bin/env python3
import Karel
# Above code is setup

# Once you complete a level, check with a programmer!
# Then, they will give you the next level
level = 5
# Want an extra challenge?
# When you get to level 3, try to get the robot to move using the
# .front_is_clear() and .check_beeper() functions


# Setup code
startPosition = {1:[10,1],2:[2,1],3:[2,11],4:[2,2],5:[16,1]}
karel = Karel.Robot(startPosition[level][0], startPosition[level][1], Karel.SOUTH, beepers=100)
world = Karel.World("worlds/level"+str(level)+".txt")
world.add_robot(karel)
world.set_speed(1)
# End setup code


# This is Karel: ►, Karel is your robot
# Your objective: Navigate through the maze to reach the end

# How do I move?
# 	There are 3 basic functions, or commands for the robot
#
#	.move() - moves the robot forward one space
# 	.turnleft() - turns the robot to the left 90 degrees
# 	.turnright() - turns the robot to the right 90 degrees
#
#	Functions (commands) for later levels:
#	.pick_beeper() - picks up a beeper (represented by symbol 'o')
#	.put_beeper() - puts down a beeper (if you have one)
#	.front_is_clear() - checks if you are able to move forward safely
#	.check_beeper() - checks if a beeper is in front of you
#	.beeper_count() - tells you the number of beepers that you have


# Put your code below:

karel.move()
karel.move()
karel.turnleft()
karel.move()
karel.move()
karel.move()
karel.turnright()
karel.move()
karel.move()