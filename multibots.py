import Karel

outer_corners = [
	(4, 2),
	(16, 2),
	(16, 8),
	(4, 8)
]
inner_corners = [
	(7, 3),
	(13, 3),
	(13, 7),
	(7, 7)
]
outer_karels = [
	Karel.Robot(outer_corners[0][0], outer_corners[0][1], Karel.EAST),  # 3>1
	Karel.Robot(outer_corners[1][0], outer_corners[1][1], Karel.SOUTH), # 2>2
	Karel.Robot(outer_corners[2][0], outer_corners[2][1], Karel.WEST),  # 1>3
	Karel.Robot(outer_corners[3][0], outer_corners[3][1], Karel.NORTH), # 0>0
]
inner_karels = [
	Karel.Robot(inner_corners[0][0], inner_corners[0][1], Karel.SOUTH), # 2>3
	Karel.Robot(inner_corners[1][0], inner_corners[1][1], Karel.WEST),  # 1>0
	Karel.Robot(inner_corners[2][0], inner_corners[2][1], Karel.NORTH), # 0>1
	Karel.Robot(inner_corners[3][0], inner_corners[3][1], Karel.EAST),  # 3>2
]
center_karel = Karel.Robot(10, 5, Karel.NORTH)

world = Karel.World("worlds/10x20-room-closed.txt",
	outer_karels + inner_karels + [center_karel]
);


while True:
	world.speed = 0
	for karel in outer_karels:
		karel.move()
		if (karel.x, karel.y) == outer_corners[-karel.dir]:
			karel.turnleft()
			karel.turnleft()
			karel.turnleft()
	for karel in inner_karels:
		karel.move()
		if (karel.x, karel.y) == inner_corners[-(karel.dir - 1) % 4]:
			karel.turnleft()
	world.set_speed(1)
	center_karel.turnleft()
