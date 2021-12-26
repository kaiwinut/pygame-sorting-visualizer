from config import *


def create_rect(i, v, n):
	width = (WINDOW_WIDTH - PADDING * 2) // n
	left = PADDING + i * width
	height = int(WINDOW_HEIGHT * (4 / 5) * (v / n))
	top = WINDOW_HEIGHT - height
	return (left, top, width, height)


def counter(l):
	for i in range(len(l)):
		yield l, i