class cpu:
    def __init__(self, alu):
        self.alu = alu
        self.instrucciones = {"LOAD": "Carga un valor en el registro",
                               "ADD": "Suma dos valores de registro",
                               "SUB": "Resta dos valores de registro",
                               "STORE": "Guarda el registro en memoria",
                               "JMP": "Salta de posicion en programa",
                               "HALT": "Rompe el bucle"}
        self.memoria = []
        self.datos = []
        self.registros = {"R0": 0,"R1": 0,"R2": 0,"R3": 0}
        self.pc = 0
    def Conjunto(self, instruccion, registro, valor):
        if instruccion == "LOAD":
            self.registros[registro] = valor
        elif instruccion == "ADD":
            self.registros[registro] = self.alu.suma(self.registros[registro], valor)
        elif instruccion == "SUB":
            self.registros[registro] = self.alu.resta(self.registros[registro], valor)
        elif instruccion == "STORE":
            self.datos.append(self.registros[registro])
        elif instruccion == "JMP":
            self.pc = valor
        elif instruccion == "HALT":
            raise ValueError("Se ha detenido el programa")
    def fetch(self):
        if len(self.memoria) == self.pc:
            raise ValueError("No hay mas espacio en memoria")
        pos = self.memoria[self.pc]
        self.pc += 1
        return pos
    def decode(self, pos):
        instruccion = pos[0]
        if len(pos) == 1:
            registro = None
            valor = None
        else:
            if str(pos[1]).startswith("R"):
                registro = pos[1]
                valor = pos[2] if len(pos) == 3 else None
            else:
                registro = None
                valor = pos[1]
        return instruccion, registro, valor
    def execute(self, instruccion, registro, valor):
        self.Conjunto(instruccion,registro, valor)
    def run(self):
        try:
            while True:
                pos = self.fetch()
                instruccion, registro, valor = self.decode(pos)
                self.execute(instruccion, registro, valor)
                print(self.registros)
        except ValueError as e:
            print("No hay mas espacio en memoria")
        print(self.memoria, self.datos)
            
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
    cpu1.memoria = [("LOAD", "R2", 3), ("LOAD", "R3", 1),("ADD", "R3",2),("STORE","R2"),("ADD", "R1",7),("SUB", "R1",2),("HALT")]
    cpu1.run()
main()