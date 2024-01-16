
class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if (s or "").find("-$") else 1

    def add(self, x):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5

    def same(self, other):
        n12 = self.n + other.n
        pooledSd = (((self.n - 1) * self.div() ** 2 + (other.n - 1) * other.div() ** 2) / (n12 - 2)) ** 0.5
        correction = 1 if n12 >= 50 else (n12 - 3) / (n12 - 2.25)
        return abs(self.mu - other.mu) / pooledSd * correction <= the.cohen

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)
