# En este documento estudiaremos un poco sobre el polimorfismo

# Polimorfismo: Es la habilidad de tomar varias formas

# Ejemplo: Tenemos una clase llamada Persona, y dos clases que heredan de Persona, que son Estudiante y Profesor

# Creamos la clase Persona que se hereadará a las otras dos clases
class Persona:

    # Definimos el método __init__ para inicializar los atributos de la clase
    # Self es una palabra reservada que se utiliza para indicar que se está trabajando con los atributos de la clase
    def datos(self):

        # Pass es una palabra reservada que se utiliza para indicar que no se va a hacer nada
        pass
        



# Creamos una clase que hereda de Persona
class Paredes(Persona):


    # Definimos el método __init__ para inicializar los atributos de la clase
    def __init__(self, nombre, edad, sexo):

        # Definimos los atributos de la clase
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo



    # Creamos una función para mostrar los datos de la persona creada
    def datos(self):

        # Retornamos los datos de la persona creada
        # format es una función que nos permite darle formato a un string para que se muestre de la manera que queramos
        return "Nombre: {}, Edad: {}, Sexo: {}".format(self.nombre, self.edad, self.sexo)




# Creamos una clase que hereda de Persona
class Deivib(Persona):


    # Definimos el método __init__ para inicializar los atributos de la clase
    def __init__(self, nombre, nacionalidad, color):

        # Definimos los atributos de la clase
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.color = color



    # Creamos una función para mostrar los datos de la persona creada
    def datos(self):

        # Retornamos los datos de la persona creada
        # format es una función que nos permite darle formato a un string para que se muestre de la manera que queramos
        return "Nombre: {}, Nacionalidad: {}, Color: {}".format(self.nombre, self.nacionalidad, self.color)





# Ingresamos los datos de las personas
# Persona 1
persona1 = Paredes("Eduard", 19, "Todos los dias")

# Persona 2
persona2 = Deivib("Deivib", "Ecuatoriano", "Carton")




# Mostramos los datos de la persona creada con el método datos
# Mostramos los datos de la persona 1
print("Nache = " ,persona1.datos())

# Mostramos los datos de la persona 2 
print("Nache = ", persona2.datos())