def solution(price):

    price = int(str(price).replace(',', ''))
    if 300000 > price >= 100000:
        a = price- (price*0.05)
        return int(a)

    elif 500000 > price >= 300000 :
        a = price - (price*0.1)
        return int(a)

    elif price >= 500000:
        a = price - (price*0.2)
        return int(a)
    else:
        return price
