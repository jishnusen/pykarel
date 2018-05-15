#
# Karel.py
#
# Copyright (c) 2017 cpiehl
#
# A Python implementation of the educational programming language Karel
#   https://en.wikipedia.org/wiki/Karel_(programming_language)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
import time

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

class World:
	symbols = {
		"wall": "#",
		"beeper": "o",
		"path": " "
	}

	def __init__(self, filename, robots=[]):
		self.grid = []
		self.height = 0
		self.width = 0
		self.step_delay = 0.5
		self.robots = []
		self.breakpoint = False
		self.step = False

		with open(filename, 'r') as f:
			self.grid = [list(line[:-1]) for line in f.readlines()]

		self.height = len(self.grid)
		self.width = len(self.grid[0])

		for robot in robots:
			self.add_robot(robot)

		self.print_world(fast=True)


	def add_robot(self, robot):
		'''Add robot to world'''
		robot.world = self
		if robot.x < 0:
			robot.x = self.width + robot.x
		if robot.y < 0:
			robot.y = self.height + robot.y
		if 0 > robot.x >= self.width:
			raise ValueError("X value outside world boundaries!")
		if 0 > robot.y >= self.height:
			raise ValueError("Y value outside world boundaries!")
		if self.grid[robot.y][robot.x] == World.symbols["wall"]:
			raise ValueError("Robot placed on a wall!")
		if self.grid[robot.y][robot.x] in Robot.dirs:
			raise ValueError("Robot placed on another robot!")

		self.robots.append(robot)
		self.print_world(fast=True)

	def set_speed(self, speed):
		'''Sets world simulation speed to a range [1, 4]'''
		speeds = [0.5, 0.15, 0.03, 0]
		try:
			self.step_delay = speeds[speed-1]
		except IndexError:
			pass

	def print_world(self, fast=False):
		output = "\n"*100
		lines = []

		for y in range(self.height):
			lines.append(self.grid[y][:])

		for robot in self.robots:
			lines[robot.y][robot.x] = Robot.dirs[robot.dir]

		for line in lines:
			output += ''.join(line) + '\n'

		if self.breakpoint or self.step:
			output += "Press ENTER to continue."
			print(output, end="")
			input()
			self.breakpoint = False
		else:
			if not fast:
				time.sleep(self.step_delay)
			print(output, end="")

	def add_breakpoint(self):
		'''Adds single breakpoint, press ENTER to continue'''
		self.breakpoint = True

	def begin_step(self):
		'''Adds breakpoints between all commands until end_step()'''
		self.step = True

	def end_step(self):
		'''Resume running commands normally'''
		self.step = False


class Robot:

	dirs = {
		NORTH: '▲',
		WEST:  '◄',
		SOUTH: '▼',
		EAST:  '►'
	}
	#~ dirs = ['^', '<', 'v', '>']
	moves = {
		NORTH: {'x': 0, 'y':-1},
		WEST:  {'x':-1, 'y': 0},
		SOUTH: {'x': 0, 'y': 1},
		EAST:  {'x': 1, 'y': 0}
	}

	class PutBeeperError(BaseException):
		pass
	class PickBeeperError(BaseException):
		pass
	class OutOfBeepersError(BaseException):
		pass
	class MovementError(BaseException):
		pass

	def __init__(self, x, y, dir, beepers=0):
		self.dir = dir # 0 = N, 1 = W, 2 = S, 3 = E
		self.x = x-1
		self.y = y-1
		self.beepercount = beepers

	def front_is_clear(self):
		'''Return True if space in front of robot can be moved into'''
		newx = self.x + Robot.moves[self.dir]['x']
		newy = self.y + Robot.moves[self.dir]['y']
		if 0 <= newx < self.world.width and 0 <= newy < self.world.height:
			if self.world.grid[newy][newx] != World.symbols["wall"]:
				for robot in self.world.robots:
					if robot.x == newx and robot.y == newy:
						return False
				return True
		return False

	def move(self):
		'''Move robot forward one step'''
		if not Robot.front_is_clear(self):
			raise Robot.MovementError("Movement blocked!")
		self.x += Robot.moves[self.dir]['x']
		self.y += Robot.moves[self.dir]['y']
		self.world.print_world()

	def turnleft(self):
		'''Rotate robot 90 degrees left'''
		self.dir = (self.dir + 1) % 4
		self.world.print_world()

	def turnright(self):
		'''Rotate robot 90 degrees left'''
		self.dir = (self.dir - 1) % 4
		self.world.print_world()

	def check_beeper(self):
		'''Return True if space in front contains a beeper'''
		newx = self.x + Robot.moves[self.dir]['x']
		newy = self.y + Robot.moves[self.dir]['y']
		if 0 <= newx < self.world.width and 0 <= newy < self.world.height:
			if self.world.grid[newy][newx] == World.symbols["beeper"]:
				for robot in self.world.robots:
					if robot.x == newx and robot.y == newy:
						return False
				return True
		return False

	def beeper_count(self):
		return self.beepercount

	def pick_beeper(self):
		'''Pick up beeper in front of robot and add it to the beeper storage'''
		if not self.check_beeper():
			raise Robot.PickBeeperError("No beeper at location!")
		newx = self.x + Robot.moves[self.dir]['x']
		newy = self.y + Robot.moves[self.dir]['y']
		self.world.grid[newy][newx] = World.symbols["path"]
		self.beepercount += 1
		self.world.print_world()

	def put_beeper(self):
		'''Place beeper from robot's beeper storage in front of the robot'''
		if not self.front_is_clear():
			raise Robot.PutBeeperError("No space to place beeper!")
		if self.check_beeper():
			raise Robot.PutBeeperError("Space already contains beeper!")
		if self.beepercount < 1:
			raise Robot.OutOfBeepersError("Not carrying any beepers!")
		newx = self.x + Robot.moves[self.dir]['x']
		newy = self.y + Robot.moves[self.dir]['y']
		self.world.grid[newy][newx] = World.symbols["beeper"]
		self.beepercount -= 1
		self.world.print_world()
