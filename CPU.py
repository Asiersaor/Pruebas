class cpu:
    def __init__(self, alu):
        self.alu = alu
        self.instrucciones = {"LOAD": "Carga un valor en el registro",
                               "ADD": "Suma dos valores de registro",
                               "SUB": "Resta dos valores de registro",
                               "STORE": "Guarda el registro en memoria",
                               "JMP": "Salta de posicion en programa"}
        self.memoria = []
        self.registros = {"R0": 0,"R1": 0,"R2": 0,"R3": 0}
        self.pc = 0
    def instrucciones(self, instruccion, registro, valor):
        if instruccion == "LOAD":
            self.registros[registro] = valor
        elif instruccion == "ADD":
            self.registros[registro] = self.alu.suma(self.registros[registro], valor)
        elif instruccion == "SUB":
            self.registros[registro] = self.alu.resta(self.registros[registro], valor)
        elif instruccion == "STORE":
            self.memoria.append(self.registros[registro])
        elif instruccion == "JMP":
            self.pc = valor
    def fetch(self):
        pos = self.memoria[self.pc]
        self.pc =+ 1
        return pos
    def decode(self, pos):
        instruccion = pos[0]
        registro = pos[1]
        valor = pos[2]
        return instruccion, registro, valor
    def execute(self, instruccion, registro, valor):
        self.instrucciones(instruccion,registro, valor)
    def run(self):
        while True:
            self.fetch()
            self.decode()
            self.execute()
class alu:
    def suma(self, valor1, valor2):
        return valor1 + valor2
    def resta(self, valor1, valor2):
        return valor1 - valor2
    def multiplicacion(self, valor1, valor2):
        return valor1 * valor2
    def division(self, valor1, valor2):
        return valor1 / valor2                 
def main():
    alu1 = alu()
    cpu1 = cpu(alu1)
    cpu1.instrucciones("LOAD", "RO", 5)