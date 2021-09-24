class Platform:
    def __init__(self, y, x1, x2):
        self.y = y
        self.x1 = x1
        self.x2 = x2
    
    def compare(self, plat):
        lDist = self.y
        rDist = self.y
        if self.y <= plat.y:
            return lDist, rDist
        if plat.x1 <= self.x1 + 0.5 <= plat.x2:
            lDist = self.y - plat.y
        if plat.x1 <= self.x2 - 0.5 <= plat.x2:
            rDist = self.y - plat.y
        return lDist, rDist

platforms = []
n = int(input())
for _ in range(n):
    y, x1, x2 = map(int, input().split())
    platforms.append(Platform(y, x1, x2))
    height = 0

for i in range(n):
    bestL = platforms[i].y
    bestR = platforms[i].y
    for j in range(n):
        if i != j:
            l, r = platforms[i].compare(platforms[j])
            bestL = min(bestL, l)
            bestR = min(bestR, r)
    height += bestL + bestR
print(height)