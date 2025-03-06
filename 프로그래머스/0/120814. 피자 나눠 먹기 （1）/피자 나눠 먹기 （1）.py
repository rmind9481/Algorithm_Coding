def solution(n):
	pizza = 7
	answer = 0
	if pizza/n < 1 :
		answer	= int((pizza+(n-1))/7)
	else:
		answer	= int(pizza/7)
	return answer