import random
from cpm import CPM


if __name__ == '__main__':
    m1 = CPM(zid=1, memoria=128, media=90, desvio=40, n=0.5,
             tc=0.4, tm=3.0, h=0.7)

    m2 = CPM(zid=2, memoria=64, media=110, desvio=20, n=0.7,
             tc=0.4, tm=3.0, h=0.7)
    random.seed(222140071)

    output = [
        'prog;tam_prog1;tam_prog2;temp1;temp2;indice_ocup1;indice_ocup2;' +
        'fator1;fator2;t_medio1;t_medio2;num_acessos;r1;r2;r3;Z1;Z2;' +
        'teta1;teta2\n'
    ]

    template = '{prog};{tam_prog1};{tam_prog2};{temp1};{temp2};' +\
        '{indice_ocup1};{indice_ocup2};{fator1};{fator2};{t_medio1};' +\
        '{t_medio2};{num_acessos};{r1};{r2};{r3};{z1};{z2};{teta1};{teta2}\n'

    for i in range(1, 21):
        csv = {
            'prog': i,
            'num_acessos': random.triangular(4, 20, 12),
            'r1': random.random(),
            'r2': random.random(),
            'r3': random.random()
        }

        m1.calcular(r1=csv['r1'], r2=csv['r2'], r3=csv['r3'],
                    num_acessos=csv['num_acessos'])
        m2.calcular(r1=csv['r1'], r2=csv['r2'], r3=csv['r3'],
                    num_acessos=csv['num_acessos'])

        csv.update(m1.as_dict())
        csv.update(m2.as_dict())

        output.append(template.format(**csv))

    with open('output.csv', 'w') as f:
        f.writelines(output)

    print('fim')
