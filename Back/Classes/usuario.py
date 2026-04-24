from .base import Base

class Usuario(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, apellido, mail, contraseña, tableros):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contraseña = contraseña
        self.tableros = tableros

    

    

