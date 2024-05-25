class Maquinas:
  def __init__(self,tipo,cultura,potencia_vazao,area_ha,th):
    self.tipo  =  tipo
    self.cultura = cultura
    self.area_ha = area_ha
    self.th = th
    self.ligado = False

  def ligar(self):
    self.ligado = True
    print(f"{self.tipo} {self.cultura} Ligado.")

  def desligar(self):
    self.ligado = False
    print(f"{self.tipo} {self.cultura} Desligado.")