import heapq

for _ in range(int(input())):
    n = int(input())
    orders = []
    shares = []
    
    s = '-'
    for i in range(n):
        line = input().split()
        type, amt, price = line[0], int(line[1]), int(line[4])
        if type == 'buy':
            heapq.heappush(orders, (-price, amt))
        else:
            heapq.heappush(shares, (price, amt))
        
        while orders and shares and -orders[0][0] >= shares[0][0]:
            s = shares[0][0]
            priceS, amtS = heapq.heappop(shares)
            priceO, amtO = heapq.heappop(orders)
            if amtS > amtO:
                heapq.heappush(shares, (priceS, amtS - amtO))
            elif amtS < amtO:
                heapq.heappush(orders, (priceO, amtO - amtS))
        
        a = shares[0][0] if shares else '-'
        b = -orders[0][0] if orders else '-'
        print(a, b, s)