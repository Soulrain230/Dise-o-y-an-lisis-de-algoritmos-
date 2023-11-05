C=[[2,1,3],
   [5,4,1],
   [3,3,4],
   [2,7,3],
   [1,9,2],
   [5,1,4],
   [7,7,3],
   [2,9,1],
   [4,8,7],
   [3,7,9]]

def calculaAreas(C):
    Areas={}
    alturas = []
    for i in range(len(C)):
        A1=C[i][0]*C[i][1]
        A2=C[i][1]*C[i][2]
        A3=C[i][2]*C[i][0]
        Areas[i]=[A1,A2,A3]
        alturas.append([C[i][2],C[i][0],C[i][1]])
    return Areas,alturas

def ordenaAreas(Areas,alturas):
    orden=[]
    for i in range(30):
        Caja = 0
        Valor = 0
        altura = 0
        for j in range(10):
            for k in range(len(Areas[j])):
                if(Areas[j][k]>Valor):
                    Caja=j
                    Valor=Areas[j][k]
                    altura = alturas[j][k]
        orden.append([Valor,Caja,altura])
        Areas[Caja].remove(Valor)
    return orden

Areas,alturas=calculaAreas(C)
orden=ordenaAreas(Areas,alturas)
for i in orden:
    print(f"Área: {i[0]}, Caja: {i[1]}, Altura: {i[2]}")
