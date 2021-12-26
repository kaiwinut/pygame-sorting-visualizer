import random

def generate_list(n):
	return random.sample([i for i in range(1, n + 1)], n)


def bubble_sort(l, ascending = True):
	for i in range(len(l)):
		for j in range(len(l) - i - 1):
			if (l[j] > l[j + 1] and ascending) or (l[j] < l[j + 1] and not ascending):
				l[j], l[j + 1] = l[j + 1], l[j]
			yield l, l[j], l[j + 1]


def selection_sort(l, ascending = True):
	for i in range(len(l)):
		min_i = i
		for j in range(i, len(l)):
			yield l, l[min_i], l[j]
			if (l[j] < l[min_i] and ascending) or (l[j] > l[min_i] and not ascending):
				min_i = j
		l[min_i], l[i] = l[i], l[min_i]



def insertion_sort(l, ascending = True):
	for i in range(len(l)):
		j = i
		while j > 0:
			if (l[j - 1] > l[j] and ascending) or (l[j - 1] < l[j] and not ascending):
				l[j - 1], l[j] = l[j], l[j - 1]
			yield l, l[j - 1], l[j]
			j -= 1


if __name__ == '__main__':
	l = generate_list(10)
	l_sorted = insertion_sort(l, ascending = True)
	while True:
		try:
			l_sorting = next(l_sorted)
		except StopIteration:
			break
		print(l_sorting)