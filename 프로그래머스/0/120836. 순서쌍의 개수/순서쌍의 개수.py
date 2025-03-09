def solution(n):
    count = 0
    for i in range(1,n+1):
        j = n%i
        if j == 0 :
            count +=1
    return count