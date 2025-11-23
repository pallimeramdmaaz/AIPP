def count_down(n):
	"""Print numbers from n down to 0 (inclusive)."""
	while n >= 0:
		print(n)
		n -= 1

if __name__ == "__main__":
	# example usage
	count_down(5)
