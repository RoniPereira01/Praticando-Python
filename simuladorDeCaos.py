import random

class Academia:
    def __ini__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 ==0]
        self.porta_halteres = {}
        self.reniciar_o_dia()

    def reniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return (i for i in self.porta_halteres.values() if i != 0)
    
    def pegar_halteres(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_alteres[key_halt] = 0
        return peso
    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos]= peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.item() if i != j]
        return len(num_caos) / len(self.porta_halteres)





self = Academia()