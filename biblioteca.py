#Gustavo Villa 
#Jose Hidalgo
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Abstracción
class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = disponible

    # Encapsulamiento: getters y setters
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def is_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible

    @abstractmethod
    def calcular_fecha_devolucion(self):
        pass

    @abstractmethod
    def obtener_tipo(self):
        pass

    @abstractmethod
    def obtener_detalles(self):
        pass

# Herencia y Polimorfismo
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, isbn, disponible=True):
        super().__init__(titulo, autor, disponible)
        self.__isbn = isbn

    