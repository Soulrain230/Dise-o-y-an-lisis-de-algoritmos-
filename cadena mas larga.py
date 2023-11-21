cad2="uhasdfkuhfkuahflikhfohfmsdflknsdfhdjfkdjfihfkjsdbgifujdfdUFJHBDJHTÑKJDHGJGHÑGJOÑUHGOUHEROGHDSJGHnglnfgjbngkjdgkdfjgdfgdfgdfgd"
cad1="fohfmsdflknsdfhdjfkdjfihfkjsdbgifujdfdUFJHBDJHTÑasdfghjklwerfgthjkdfghjkwttweyeyue"

cadena1 = list(cad1)
cadena2 = list(cad2)

matriz=[]
for i in range(len(cadena1)):
    fila=[]
    for j in range(len(cadena2)):
        fila.append(0)
    matriz.append(fila)


for i in range(len(cadena1)):
    for j in range(len(cadena2)):
        if(i==0 or j==0):
            if(cadena1[i]==cadena2[j]):
                matriz[i][j]=1
            else:
                if(cadena1[i]==cadena2[j]):
                    matriz[i][j]=1+ matriz[i-1]

cadmax= 0
im=0
jm=0
for i in range(len(cadena1)):
    for j in range(len(cadena2)):
        if(cadmax<matriz[i][j]):
            cadmax=matriz[i][j]
            im=i
            jm=j
print(cadmax,im,jm)
#print(cad1[im-cadmax+1:(im-cadmax+1)+cadmax])