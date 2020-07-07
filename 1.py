def gcdAll(w):
    mm = min(w)
    res = -1
    for ii in range(mm, 0, -1):
        all = True
        res = ii
        for j in w:
            if j % res != 0:
                all = False
                res = -1
                break
        if all == True:
            break
    return res

class WRR:
    def __init__(self, w):
        self.w = w
        self.i = -1
        self.cw = 0

    def nextServer(self):
        while True:
            self.i = (self.i + 1) % len(self.w)
            if self.i == 0:
                self.cw = self.cw - gcdAll(self.w)
                if self.cw <= 0: 
                    self.cw = max(self.w)
                    if self.cw == 0: return -1

            if self.w[self.i] >= self.cw: return self.i

    def status(self):
        return "current weight: {0}, last used server: {1}".format(self.cw, self.i)
    


wrr = WRR([30, 20, 40, 10])
arr = [0, 0, 0, 0]
for clientId in range(0, 100, 1):
    serverId = wrr.nextServer()
    arr[serverId] += 1
    print("client with id: {0} served by: {1}".format(clientId, serverId))
    #print(serverId)
    #print(wrr.status())
print(arr)
