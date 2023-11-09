N = ["N1","N2","N3","N4","N5"]
K = ["K1","K2","K3","K4","K5"]

N1 = ["K2","K3","K1","K5","K4"]
N2 = ["K3","K5","K1","K4","K2"]
N3 = ["K5","K3","K4","K2","K1"]
N4 = ["K1","K2","K3","K4","K5"]
N5 = ["K4","K3","K2","K1","K5"]

K1 = ["N1","N2","N4","N5","N3"]
K2 = ["N3","N1","N2","N5","N4"]
K3 = ["N4","N2","N1","N5","N3"]
K4 = ["N3","N1","N2","N4","N5"]
K5 = ["N5","N4","N1","N3","N2"]

solteros = ["N1","N2","N3","N4","N5"]

rankingsN = [N1,N2,N3,N4,N5]
rankingsK = [K1,K2,K3,K4,K5]


def fase1(solteros, rankingsN, rankingsK):
    parejas = {}  
    aux=solteros.copy()
    for i in range(len(aux)):
        pareja = int(rankingsN[i][0].replace("K", ""))-1
        if(rankingsK[pareja][0] == aux[i]):
            parejas[pareja] = aux[i]
            solteros.remove(i)
    return parejas,solteros