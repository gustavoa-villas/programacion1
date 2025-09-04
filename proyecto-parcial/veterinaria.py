from abc import ABC, abstractmethod
from datetime import datetime

# Clase abstracta
class Veterinaria(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def calcular_precio_consulta(self):
        pass

# Cliente
class Cliente(Veterinaria):
    def __init__(self, nombre, telefono):
        self.__nombre = nombre
        self.__telefono = telefono
    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Teléfono: {self.__telefono}"

    def calcular_precio_consulta(self):
        return 0  # No aplica

# Mascota
class Mascota(Veterinaria):
    def __init__(self, nombre, especie, edad, propietario: Cliente):
        self.__nombre = nombre
        self.__especie = especie.lower()
        self.__edad = edad
        self.__propietario = propietario

    def get_nombre(self):
        return self.__nombre

    def get_especie(self):
        return self.__especie
    def mostrar_info(self):
        return (f"Mascota: {self.__nombre}, Especie: {self.__especie}, Edad: {self.__edad} años, "
                f"Propietario: {self.__propietario.get_nombre()}")

    def calcular_precio_consulta(self):
        precios = {
            "perro": 50000,
            "gato": 45000,
            "ave": 30000,
            "conejo": 35000,
            "reptil": 60000
        }
        return precios.get(self.__especie, 40000)  # Precio por defecto

# Veterinario
class Veterinario(Veterinaria):
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre
        self.__especialidad = especialidad

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"Veterinario: {self.__nombre}, Especialidad: {self.__especialidad}"

    def calcular_precio_consulta(self):
        return 0  # No aplica

# Consulta
class Consulta(Veterinaria):
    def __init__(self, mascota: Mascota, veterinario: Veterinario, fecha: datetime, motivo: str):
        self.__mascota = mascota
        self.__veterinario = veterinario
        self.__fecha = fecha
        self.__motivo = motivo

    def mostrar_info(self):
        precio = self.__mascota.calcular_precio_consulta()
        return (f"Consulta para {self.__mascota.get_nombre()} ({self.__mascota.get_especie()}) con el Dr. {self.__veterinario.get_nombre()} "
                f"el {self.__fecha.strftime('%d/%m/%Y')} por motivo: {self.__motivo}. Precio: ${precio}")

    def calcular_precio_consulta(self):
        return self.__mascota.calcular_precio_consulta()

#Implementación
if __name__ == "__main__":
    cliente1 = Cliente("Laura Gómez", "3124567890")
    mascota1 = Mascota("Firulais", "Perro", 5, cliente1)
    mascota2 = Mascota("Michi", "Gato", 3, cliente1)
    vet1 = Veterinario("Ramírez", "Dermatología")
    consulta1 = Consulta(mascota1, vet1, datetime.now(), "Revisión de piel")
    consulta2 = Consulta(mascota2, vet1, datetime.now(), "Chequeo general")

    for entidad in [consulta1, consulta2]:
        print(entidad.mostrar_info())
