from .base import Base

class Estado(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, tablero, posicion, tareas):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.tablero = tablero
        self.posicion = posicion
        self.tareas = tareas

    def crear_estado(self):
        pass

    def eliminar_estado(self):
        pass