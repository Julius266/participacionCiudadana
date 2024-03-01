from sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pais(db.Model):
    #datos
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)
    codigo = db.Column(db.String(10),unique = True, nullable=True)
    #relaciones
    provincias = db.relationship('Provincia', backref='pais', lazy=True)
    #funcion repr
    def __repr__(self):
        return f'<Pais {self.id}, Nombre: {self.nombre}, Código: {self.codigo}>'
    
    

class Provincia(db.Model):
    #datos
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)
    codigo = db.Column(db.String(10),unique = True, nullable=True)
    #relaciones
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    #funcion repr
    def __repr__(self):
        return f'<Provincia {self.id}, Nombre: {self.nombre}, Código: {self.codigo}>'
    

class Canton(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)
    codigo = db.Column(db.String(10),unique = True, nullable=True)

    def __repr__(self):
        return f'<Canton {self.id}, Nombre: {self.nombre}, Código: {self.codigo}>'



class Parroquia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)

    def __repr__(self):
        return f'<Parroquia {self.id}, Nombre: {self.nombre}>'


class Comunidad(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)

    def __repr__(self):
        return f'<Comunidad {self.id}, Nombre: {self.nombre}>'
    


class Sitio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)
    tenencia = db.Column(db.Boolean, default=False, nullable=False)
    numero_persona = db.Column(db.Integer, unique =True, nullable =True)
    
    def __repr__(self):
        return f'<Sitio {self.id}, Nombre: {self.nombre}, Tenencia: {self.tenencia}, Número de Persona: {self.numero_persona}>'

    


class Actor_social(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)
    correo = db.Column(db.String(60), unique = True, nullable=True)
    Contacto = db.Column(db.String(10), unique =True, nullable =True)
    firma = db.Column(db.String(100), unique = True, nullable = True)

    def __repr__(self):
        return f'<Actor_social {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Contacto: {self.contacto}, Firma: {self.firma}>'


class Tipo_de_actor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),unique = True, nullable=True)

    def __repr__(self):
        return f'<Tipo_de_actor {self.id}, Nombre: {self.nombre}>'
    


class usuario(db.Model):
    #datos
    id = db.Colum(db.Integer, primary_key = True)
    nombre = db.Colum(db.String(30), nullable = False)
    apellido = db.Colum(db.String(30), nullable = False)
    contacto = db.Colum(db.Integer, nullable =True)
    #relaciones
    #funcion repr
    def __repr__(self):
        return f'<Usuario {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Contacto: {self.contacto}>'

class rol_usuario(db.Model):
    #datos
    id = db.Colum(db.Integer, primary_key = True)
    nombre = db.Colum(db.String(30), nullable = True)
    #relaciones
    #funcion repr


class asignacion_gestores(db.Model):
    #datos
    id = db.Colum(db.Integer, primary_key = True)
    #relaciones

    #funcion repr

class informe(db.Model):
    id = db.Colum(db.Integer, primary_key = True)
    Atribucion = db.Colum(db.String(300), nullable = False)
    numero_persona = db.Colum(db.Integer, nullable = False)
    fecha = db.Colum(db.Date, nullable = True)
    hora = db. Colum(db.Date, nullable =  True)
    duracion = db.Colum(db.String, nullable = False)
    descripcion_actividades = db.Colum(db.String(400), nullable = True)
    alertas = db.Colum(db.String(200), nullable = True)
    recomendaciones = db.Colum(db.String(400), nullable = False)
    elaborado_por = db.Colum(db.String(200), nullable = False)
    revisado_por = db.Colum(db.String(200), nullable = False)
    aprobado_por = db.Colum(db.String(200), nullable = False)
    
class departamento(db.Model):
    id = db.Colum(db.Integer, primary_key = True)
    nombre = db.Colum(db.String(30), nullable = True)

class asignacion_departamento(db.Model):
    id = db.Colum(db.Integer, primary_key = True)


class PDOT(db.Model):
    id = db.Colum(db.Integer, primary_key = True)
    nombre = db.Colum(db.String, primary_key = True)

class obra_proyecto(db.Model):
    id = db.Colum(db.Integer, primary_key = True)
    nombre = db.Colum(db.String, nullable = False)





       
