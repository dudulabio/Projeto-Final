from maquinas import Maquinas

class Pivo(Maquinas):
        
    def __init__(self,tipo,cultura, potencia_vazao,area_ha,th):
       super().__init__(tipo,cultura,potencia_vazao,area_ha,th)
       self.potencia_vazao = potencia_vazao


    def imprimir(self):
            print(f"Tipo: {self.tipo}")
            print(f'Talhão: {self.th}')
            print(f'Cultura: {self.cultura}')
            print(f'Capacidade de vazão: {self.potencia_vazao}')
            print(f'Área em HA: {self.area_ha}')

    def irrigar(self):
        if self.ligado:
                print(f"{self.tipo} {self.cultura} irrigando.")
        else:
                print("Pivo está irrigando")

    def desligar_pivo(self):
            self.desligar()

