from .base import Base

class Tablero(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, descripcion, listas, propietario):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.descripcion = descripcion
        self.listas = listas
        self.propietario = propietario


    def crear_tablero(self):
        pass

    def eliminar_tablero(self):
        pass