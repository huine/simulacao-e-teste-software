from random import randint


class MeioQuadrado():
    """."""

    def __init__(self, seed=randint(1000, 9999)):
        self.seed = int(seed)

    def gerar(self):
        """."""
        self.seed = int(str(self.seed ** 2)[2:6])

        if self.seed == 0 or self.seed < 1000:
            self.seed = randint(1000, 9999)

        return float(self.seed)/9999


class LCG():
    """."""

    def __init__(self, seed=randint(0, 999999999), const_m=3, const_a=1,
                 m=randint(111111111, 999999999)):
        """."""
        self.seed = int(seed)
        self.const_m = float(const_m)
        self.const_a = float(const_a)
        self.m = int(m)
        self.ult = None

    def gerar(self, dec=False):
        """."""
        if self.ult is None:
            self.ult = self.seed

        self.ult = (self.const_m * self.ult + self.const_a) % self.m

        if dec:
            return self.ult/float(self.m)

        return self.ult
