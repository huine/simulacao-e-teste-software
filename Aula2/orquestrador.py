from math import pi, log, pow, cos
from gerador import LCG, MeioQuadrado
import random


class CPM():
    """."""

    def __init__(self, memoria, media, desvio, n):
        """."""
        self.memoria = float(memoria)
        self.media = float(media)
        self.desvio = float(desvio)
        self.n = float(n)
        self.z = None
        self.m = None
        self.t = None
        self.teta = None

    def resolve_z(self, r1, r2):
        """."""
        self.z = pow((-2 * log(r1)), 0.5) * cos(2 * pi * r2)

    def resolve_m(self):
        """."""
        if self.z is None:
            raise Exception("Calcular o 'z' primeiro")
        self.m = self.z * self.desvio + self.media

    def resolve_t(self, r3):
        """."""
        if self.teta is None:
            raise Exception("Calcular o 'teta' primeiro")
        self.t = -1 * self.teta * log(r3)

    def resolve_teta(self):
        """."""
        if self.m is None:
            raise Exception("Calcular o 'm' primeiro")
        self.teta = self.n * self.m


if __name__ == '__main__':
    m1 = CPM(memoria=128, media=90, desvio=40, n=0.5)
    m2 = CPM(memoria=64, media=110, desvio=20, n=0.2)
    mq = MeioQuadrado(seed=222140071)
    lcg = LCG(seed=222140071)
    random.seed(222140071)

    output = [
        'prog;tam_prog1;tam_prog2;temp1;temp2;r1;r2;r3;Z1;Z2;teta1;teta2\n'
    ]

    template = '{prog};{tam_prog1};{tam_prog2};{temp1};{temp2};{r1};' +\
        '{r2};{r3};{z1};{z2};{teta1};{teta2}\n'

    for i in range(1, 21):
        r1 = mq.gerar()
        r2 = lcg.gerar(dec=True)
        r3 = random.random()

        m1.resolve_z(r1=r1, r2=r2)
        m1.resolve_m()
        m1.resolve_teta()
        m1.resolve_t(r3=r3)

        m2.resolve_z(r1=r1, r2=r2)
        m2.resolve_m()
        m2.resolve_teta()
        m2.resolve_t(r3=r3)

        output.append(template.format(
            prog=i, tam_prog1=m1.m, tam_prog2=m2.m, temp1=m1.t,
            temp2=m2.t, r1=r1, r2=r2, r3=r3, z1=m1.z, z2=m2.z,
            teta1=m1.teta, teta2=m2.teta))

    with open('output.csv', 'w') as f:
        f.writelines(output)

    print('fim')
