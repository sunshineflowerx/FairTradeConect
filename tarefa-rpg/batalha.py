from abc import ABC, abstractmethod
class Personagem(ABC):
    def __init__(self, nome, vida, ataque_base, defesa):
        self.nome = nome
        self._vida = vida  
        self._ataque_base = ataque_base # 
        self.defesa = defesa

    @abstractmethod
    def atacar(self, outro):
        pass

    def receber_dano(self, dano):
        dano_real = max(0, dano - self.defesa)
        self._vida -= dano_real  
        print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self._vida}") 

    def esta_vivo(self):
        return self._vida > 0 

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque_base, defesa, furia):
        super().__init__(nome, vida, ataque_base, defesa)
        self.__furia = furia

    def atacar(self, alvo):
        print(f"{self.nome} ataca com espada!")
        alvo.receber_dano(self._ataque_base) 

    def ataque_especial(self, alvo):
        if self.__furia >= 10:
            print(f"{self.nome} usa ataque especial!")
            alvo.receber_dano(self._ataque_base * 2) 
            self.__furia -= 10
        else:
            print(f"{self.nome} não tem fúria suficiente!")

class Mago(Personagem):
    def __init__(self, nome, vida, ataque_base, defesa, mana):
        super().__init__(nome, vida, ataque_base, defesa)
        self.__mana = mana

    def atacar(self, alvo):
        if self.__mana >= 5:
            print(f"{self.nome} lança uma magia!")
            alvo.receber_dano(self._ataque_base + 5) 
            self.__mana -= 5
        else:
            print(f"{self.nome} está sem mana!")

guerreiro = Guerreiro("Thor", 100, 15, 10, 30)
mago = Mago("Merlin", 80, 10, 5, 40)

while guerreiro.esta_vivo() and mago.esta_vivo():
    guerreiro.atacar(mago)
    if mago.esta_vivo():
        mago.atacar(guerreiro)

print("Batalha encerrada!")