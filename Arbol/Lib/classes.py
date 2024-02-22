class modo():
    def __init__(self,valor):
        self.valor=valor
        self.izquierda = None
        self.Derecha= None
        pass
    def __str__(self):
        return f'Valor:  {self.valor}'
    
    def getArbol(self):
        strOut = ''
        strOut += f'NP: [{self.valor}] '
        if type(self.izquierda) != type(None):
            strOut += f'Iz: [{self.valor}] -> [{self.izquierda}]'
        if self.Derecha is not None:
            strOut += f'Dr: [{self.valor}] -> [{self.Derecha}]'
        return strOut
    def __str__(self):
        return f'{self.valor}'
        
