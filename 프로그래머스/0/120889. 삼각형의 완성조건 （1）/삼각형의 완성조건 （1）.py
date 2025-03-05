
def solution(sides):
    
	max_value = max(sides)
	sides.remove(max_value)
	a = sum(sides)
	if max_value < a:
		return 1

	else:
		return 2


