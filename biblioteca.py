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

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=15)

    def obtener_tipo(self):
        return "Libro"

    def obtener_detalles(self):
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, ISBN: {self.__isbn}"

class Revista(MaterialBiblioteca):
    def _init_(self, titulo, autor, numero, disponible=True):
        super()._init_(titulo, autor, disponible)
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=7)

    def obtener_tipo(self):
        return "Revista"

    def obtener_detalles(self):
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, Número: {self.__numero}"

class MaterialAudiovisual(MaterialBiblioteca):
    def _init_(self, titulo, autor, formato, disponible=True):
        super()._init_(titulo, autor, disponible)
        self.__formato = formato

    def get_formato(self):
        return self.__formato

    def set_formato(self, formato):
        self.__formato = formato

    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=3)

    def obtener_tipo(self):
        return "Material Audiovisual"

    def obtener_detalles(self):
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, Formato: {self.__formato}"

# Ejemplo de uso
if _name_ == "_main_":
    libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "123456789")
    revista = Revista("National Geographic", "Varios", 202)
    audiovisual = MaterialAudiovisual("Documental", "BBC", "DVD")

    materiales = [libro, revista, audiovisual]
    for material in materiales:
        print(material.obtener_tipo())
        print(material.obtener_detalles())
        print("Fecha de devolución:", material.calcular_fecha_devolucion().strftime("%Y-%m-%d"))
        print("Disponible:", material.is_disponible())
        print("---")




    
