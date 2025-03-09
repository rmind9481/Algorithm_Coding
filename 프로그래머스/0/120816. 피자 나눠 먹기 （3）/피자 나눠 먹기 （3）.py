def solution(slice, n):
    # 먹는사람이 조각수보다 작은면
    pizza = 1
    while True:
        if slice*pizza >= n: 
            return pizza
        # 먹는사람이 조각수보다 크면
        elif slice*pizza < n :
            pizza +=1   