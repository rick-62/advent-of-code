loop:
	pytest --looponfail --capture=no

input:
	python get_puzzle_input.py $(d) $(y)