from Lib import *
inOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]
modo1 = modo(1)
modo2 = modo(2)
modo3 = modo(3)
modo4 =  modo(4)
modo5 = modo(5)
modo6 = modo(6)
modo7 = modo (7)
linkHijo(modo1,modo2,modo3)
linkHijo(modo2,modo4,modo5)
linkHijo(modo3,modo6,modo7)

LRV(modo1,PostOrderArr)
VLR(modo1,PreOrderArr)
LVR (modo1,inOrderArr)

print( inOrderArr )
print( PreOrderArr )
print( PostOrderArr)
print( modo1.getArbol())
print('-------------------------------------------------------------------------')
arrModos=[16,5,7,12,9,20,18,3,10,14]
modoRaiz = None
for i in range(0,len(arrModos),1):
    if i == 0:
        modoRaiz = modo(arrModos[i])
    else:
        modoOrdenados(modoRaiz, modo(arrModos[i]))
    pass

'''modoRaiz = modo(16)
modo9 = modo(5)
modo10 = modo(7)
modo11 = modo(12)
modo12 =  modo(9)
modo13 = modo(20)
modo14 = modo(18)
modo15 = modo (3)
modo16 = modo(10)
modo17 = modo(14)'''
print('Inicia modos Ordenados')
printArbol( modoRaiz)
'''modoOrdenados(modoRaiz,modo9)
modoOrdenados(modoRaiz,modo10)
modoOrdenados(modoRaiz,modo11)
modoOrdenados(modoRaiz,modo12)
modoOrdenados(modoRaiz,modo13)
modoOrdenados(modoRaiz,modo14)
modoOrdenados(modoRaiz,modo15)
modoOrdenados(modoRaiz,modo16)
modoOrdenados(modoRaiz,modo17)
print(modoRaiz.getArbol())
print(modo9.getArbol())
print(modo10.getArbol())
print(modo11.getArbol())
print(modo12.getArbol())
print(modo13.getArbol())
print(modo14.getArbol())
print(modo15.getArbol())
print(modo16.getArbol())
print(modo17.getArbol())'''