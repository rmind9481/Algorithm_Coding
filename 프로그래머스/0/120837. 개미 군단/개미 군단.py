def solution(hp):
    count = 0
    
    count += hp // 5  # 5 공격력 개미
    hp %= 5
    
    count += hp // 3  # 3 공격력 개미
    hp %= 3
    
    count += hp  # 1 공격력 개미 (hp가 남은 만큼 필요)

    return count