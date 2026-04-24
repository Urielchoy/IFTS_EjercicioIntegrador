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

    # Metodos
    
    def cambiar_prioridad(self):
        pass

    def asignar_usuario(self):
        pass

    def cambiar_estado(self):
        pass

    def editar(self):
        pass

    def copiar_tarea(self):
        pass
