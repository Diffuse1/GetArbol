
def linkHijo( modoPradre, modoHijoIzq=None, modoHijoDer=None):
    if modoHijoIzq is not None:
        modoPradre.izquierda =modoHijoIzq
    if modoHijoDer is not None:
        modoPradre.Derecha = modoHijoDer
    pass
def LVR(modo, inOrderArr):
    if modo is not None:
        modoPadre = modo
        LVR (modoPadre.izquierda, inOrderArr)
        inOrderArr.append(modoPadre.valor)
        LVR(modoPadre.Derecha,inOrderArr)
    return inOrderArr
def VLR(modo, PreOrderArr):
    if modo is not None:
        modoPadre = modo
        PreOrderArr.append(modoPadre.valor)
        VLR(modoPadre.izquierda, PreOrderArr)
        VLR(modoPadre.Derecha,PreOrderArr)
    return PreOrderArr
def LRV(modo, PostOrderArr):
    if modo is not None:
        modoPadre = modo
        LRV(modoPadre.izquierda, PostOrderArr)
        LRV(modoPadre.Derecha,PostOrderArr)
        PostOrderArr.append(modoPadre.valor)
    return PostOrderArr
def modoOrdenados(modoPadre, newModo):
    if newModo.valor < modoPadre.valor:
        if modoPadre.izquierda is None:
            modoPadre.izquierda = newModo
        else:
            modoOrdenados(modoHijo)
        if newModo.valor > modoPadre.valor:
            modoHijo = modoPadre.Derecha
            
    if newModo.valor > modoPadre.valor:
        if modoPadre.Derecha is None:
            modoPadre.Derecha = newModo
    pass


