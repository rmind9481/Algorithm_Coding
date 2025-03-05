def solution(money):
    a = int(money/5500)
    b = int(money%5500)
    answer = []
    answer.extend([a,b])
    return answer