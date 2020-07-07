import math

class WRR:
    def __init__(self, w):
        self.w = w
        self.i = -1
        self.cw = 0
        self.n = len(w)

    def gcdS(self):
        res = self.w[0]
        for i in range(1, self.n):
            res = math.gcd(res, self.w[i])
            if res == 1: return 1
        return res
    
    def maxS(self):
        return max(self.w)

    def nextServer(self):
        while True:
            self.i = (self.i + 1) % self.n
            if self.i == 0:
                self.cw = self.cw - self.gcdS()
                if self.cw <= 0: 
                    self.cw = self.maxS()
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
    #print(wrr.status())
print(arr)

'''
Supposing that there is a server set S = {S0, S1, …, Sn-1};
W(Si) indicates the weight of Si;
i indicates the server selected last time, and i is initialized with -1;
cw is the current weight in scheduling, and cw is initialized with zero; 
max(S) is the maximum weight of all the servers in S;
gcd(S) is the greatest common divisor of all server weights in S;

while (true) {
    i = (i + 1) mod n;
    if (i == 0) {
        cw = cw - gcd(S); 
        if (cw <= 0) {
            cw = max(S);
            if (cw == 0)
            return NULL;
        }
    } 
    if (W(Si) >= cw) 
        return Si;
}
'''