from .base import Base

class Tarea(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, titulo, descripcion, estado, prioridad, usuarioAsignado, fechaVencimiento, posicion):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.titulo = titulo
        self.descripcion = descripcion 
        self.estado = estado
        self.prioridad = prioridad
        self.usuarioAsignado = usuarioAsignado
        self.fechaVencimiento = fechaVencimiento
        self.posicion = posicion

    def crear_tarea(self):
        pass

    def eliminar_tarea(self):
        pass

    def mover_tarea(self):
        pass