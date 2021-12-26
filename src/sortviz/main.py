import sys
import pygame as p
from config import *
from utils import *
from Sorting import *


def draw_sorted(window, algo, count):
	try:
		# Get current list and the numbers compared this turn
		sorted_list, i = next(count)
		n_num = len(sorted_list)

		draw_bg(window, algo)

		for j, v in enumerate(sorted_list):
			rect = p.Rect(*create_rect(j, v, n_num))
			if j <= i:
				p.draw.rect(window, PASTEL_GREEN, rect)
			else:
				p.draw.rect(window, WHITE, rect)

		p.display.flip()

	except StopIteration:
		return True	


def draw_sorting(window, curr_list, v1, v2):
	n_num = len(curr_list)
	for i, v in enumerate(curr_list):
		rect = p.Rect(*create_rect(i, v, n_num))
		if v == v1:
			p.draw.rect(window, PASTEL_PINK, rect)
		elif v == v2:
			p.draw.rect(window, PASTEL_BLUE, rect)
		else:
			p.draw.rect(window, WHITE, rect)


def draw_bg(window, algo):
	window.fill(BACKGROUND)
	comicsans = p.font.SysFont('Helvetica', 20)
	name_surface = comicsans.render(algo, False, WHITE)
	window.blit(name_surface, (20, 20))

def draw(window, algo, l, n):
	try:
		# Get current list and the numbers compared this turn
		curr_list, v1, v2 = next(l)
		draw_bg(window, algo)
		draw_sorting(window, curr_list, v1, v2)

		p.display.flip()

	except StopIteration:
		return True


def main():
	# Initialize pygame
	p.init()
	p.font.init()

	# Create pygame window
	window = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	clock = p.time.Clock()

	sorting_algorithms = {
		'Bubble Sort': bubble_sort,
		'Selection Sort': selection_sort,
		'Insertion Sort': insertion_sort,
	}

	# Initialize parameters
	n = 30
	ascending = False
	lst = generate_list(n)
	count = counter(sorted(lst, reverse = not ascending))

	algo = 'Selection Sort'
	l = sorting_algorithms[algo](lst, ascending = ascending)

	# Initialize flags
	running = True
	reset = False
	finished = False

	while running:
		clock.tick(FPS)

		if reset:
			lst = generate_list(n)
			l = bubble_sort(lst)

		for e in p.event.get():
			if e.type == p.QUIT:
				running = False
				p.quit()
				sys.exit()

		if not finished and draw(window, algo, l, n):
			finished = True

		if finished and draw_sorted(window, algo, count):
			p.time.wait(2000)
			running = False
			p.quit()

if __name__ == '__main__':
	main()