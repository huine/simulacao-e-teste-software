from math import pi, log, pow, cos


class CPM():
    """."""

    def __init__(self, zid, memoria, media, desvio, n, tc, tm, h):
        """."""
        self.id = str(zid)
        self.memoria = float(memoria)
        self.media = float(media)
        self.desvio = float(desvio)
        self.n = float(n)
        self.tc = float(tc)
        self.tm = float(tm)
        self.h = float(h)
        self.z = None
        self.m = None
        self.t = None
        self.teta = None
        self.t_medio = None
        self.indice_ocup = None
        self.fator = None

    def resolve_z(self, r1, r2):
        """."""
        self.z = pow((-2 * log(r1)), 0.5) * cos(2 * pi * r2)

    def resolve_m(self):
        """."""
        if self.z is None:
            raise Exception("Calcular o 'z' primeiro")
        self.m = self.z * self.desvio + self.media

    def resolve_t(self, r3, num_acessos):
        """."""
        if self.teta is None:
            raise Exception("Calcular o 'teta' primeiro")
        if self.t_medio is None:
            raise Exception("Calcular o 't_medio' primeiro")
        if self.fator is None or self.indice_ocup is None:
            raise Exception("Calcular o 'indice_ocup/fator' primeiro")

        self.t = ((-1 * self.teta * log(r3)) +
                  (num_acessos * self.t_medio)) * self.fator

    def resolve_teta(self):
        """."""
        if self.m is None:
            raise Exception("Calcular o 'm' primeiro")
        self.teta = self.n * self.m

    def resolve_tmedio(self):
        """."""
        self.t_medio = (self.h * self.tc) + ((1 - self.h) * self.tm)

    def fator_correcao(self):
        """."""
        if self.m is None:
            raise Exception("Calcular o 'm' primeiro")

        self.indice_ocup = (self.m * 100) / self.memoria

        if self.indice_ocup < 51:
            self.fator = 1.0
        elif self.indice_ocup >= 51 and self.indice_ocup < 76:
            self.fator = 1.5
        elif self.indice_ocup >= 76 and self.indice_ocup < 86:
            self.fator = 2.0
        else:
            self.fator = 4.0

    def calcular(self, r1, r2, r3, num_acessos):
        """."""
        self.resolve_z(r1=r1, r2=r2)
        self.resolve_tmedio()
        self.resolve_m()
        self.resolve_teta()
        self.fator_correcao()
        self.resolve_t(r3=r3, num_acessos=num_acessos)

    def as_dict(self):
        """."""
        tmp = {}
        tmp['tam_prog{}'.format(self.id)] = self.m
        tmp['temp{}'.format(self.id)] = self.t
        tmp['z{}'.format(self.id)] = self.z
        tmp['teta{}'.format(self.id)] = self.teta
        tmp['indice_ocup{}'.format(self.id)] = self.indice_ocup
        tmp['fator{}'.format(self.id)] = self.fator
        tmp['t_medio{}'.format(self.id)] = self.t_medio
        return tmp
