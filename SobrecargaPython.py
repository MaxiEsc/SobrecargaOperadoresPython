'''
La idea de la sobrecarga es que un mismo operador se comporte de distintas formas

Es aplicable en las clases segun su operador y hay que rescribir haciendo incapie en la herencia

+ --> __add__(self, other)
- --> __sub__(self, other)
* --> __mul__(self, other)
/ --> __truediv__(self, other)
// --> __floordiv__(self, other)
% --> __mod__(self, other)
** --> __pow__(self, other)

'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return f'{self.nombre} {otro.nombre}'

    def __sub__(self, otro):
        return self.edad - otro.edad


persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 20)
print(persona1 + persona2)
print(persona1 - persona2)

# obj1 + obj2
# obj1.__add__(obj2)