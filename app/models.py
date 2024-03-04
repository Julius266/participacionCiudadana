from sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    codigo = db.Column(db.String(10), unique=True, nullable=True)
    
    provincias = db.relationship('Provincia', backref='pais', lazy=True)

    def __repr__(self):
        return f'<Pais {self.id}, Nombre: {self.nombre}, Código: {self.codigo}>'

class Provincia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    codigo = db.Column(db.String(10), unique=True, nullable=True)
    
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    cantones = db.relationship('Canton', backref='provincia', lazy=True)

    def __repr__(self):
        return f'<Provincia {self.id}, Nombre: {self.nombre}, Código: {self.codigo}>'

class Canton(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    codigo = db.Column(db.String(10), unique=True, nullable=True)
    
    id_provincia = db.Column(db.Integer, db.ForeignKey('provincia.id'), nullable=False)
    parroquias = db.relationship('Parroquia', backref='canton', lazy=True)

    def __repr__(self):
        return f'<Canton {self.id}, Nombre: {self.nombre}, Código: {self.codigo}>'

class Parroquia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    
    id_canton = db.Column(db.Integer, db.ForeignKey('canton.id'), nullable=False)
    comunidades = db.relationship('Comunidad', backref='parroquia', lazy=True)

    def __repr__(self):
        return f'<Parroquia {self.id}, Nombre: {self.nombre}>'

class Comunidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    
    id_parroquia = db.Column(db.Integer, db.ForeignKey('parroquia.id'), nullable=False)
    sitios = db.relationship('Sitio', backref='comunidad', lazy=True)
    actores_sociales = db.relationship('ActorSocial', backref='comunidad', lazy=True)
    asignaciones_gestores = db.relationship('AsignacionGestores', backref='comunidad', lazy=True)
    informe = db.relationship('Informe', backref='comunidad', uselist=False)

    def __repr__(self):
        return f'<Comunidad {self.id}, Nombre: {self.nombre}>'

class Sitio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    tenencia = db.Column(db.Boolean, default=False, nullable=False)
    numero_persona = db.Column(db.Integer, unique=True, nullable=True)
    
    comunidad_id = db.Column(db.Integer, db.ForeignKey('comunidad.id'), unique=True, nullable=True)
    actor_social = db.relationship('ActorSocial', backref='sitio', uselist=False)
    asignaciones_gestores = db.relationship('AsignacionGestores', backref='sitio', lazy=True)
    informe = db.relationship('Informe', backref='sitio', uselist=False)

    def __repr__(self):
        return f'<Sitio {self.id}, Nombre: {self.nombre}, Tenencia: {self.tenencia}, Número de Persona: {self.numero_persona}>'

class ActorSocial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    correo = db.Column(db.String(60), unique=True, nullable=True)
    contacto = db.Column(db.String(10), unique=True, nullable=True)
    firma = db.Column(db.String(100), unique=True, nullable=True)
    
    comunidad_id = db.Column(db.Integer, db.ForeignKey('comunidad.id'), nullable=False)
    sitio_id = db.Column(db.Integer, db.ForeignKey('sitio.id'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('tipo_de_actor.id'))

    def __repr__(self):
        return f'<ActorSocial {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Contacto: {self.contacto}, Firma: {self.firma}>'

class TipoDeActor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True, nullable=True)
    
    actor_social = db.relationship('ActorSocial', backref='tipo_de_actor', uselist=False)

    def __repr__(self):
        return f'<TipoDeActor {self.id}, Nombre: {self.nombre}>'

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    contacto = db.Column(db.Integer, nullable=True)
    
    asignacion_gestores = db.relationship('AsignacionGestores', backref='usuario', lazy=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol_usuario.id'))

    def __repr__(self):
        return f'<Usuario {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Contacto: {self.contacto}>'

class RolUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=True)
    
    usuarios = db.relationship('Usuario', backref='rol_usuario', lazy=True)

class AsignacionGestores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    comunidad_id = db.Column(db.Integer, db.ForeignKey('comunidad.id'))
    sitio_id = db.Column(db.Integer, db.ForeignKey('sitio.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Informe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atribucion = db.Column(db.String(300), nullable=False)
    numero_persona = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=True)
    hora = db.Column(db.Date, nullable=True)
    duracion = db.Column(db.String, nullable=False)
    descripcion_actividades = db.Column(db.String(400), nullable=True)
    alertas = db.Column(db.String(200), nullable=True)
    recomendaciones = db.Column(db.String(400), nullable=False)
    elaborado_por = db.Column(db.String(200), nullable=False)
    revisado_por = db.Column(db.String(200), nullable=False)
    aprobado_por = db.Column(db.String(200), nullable=False)
    
    sitio_id = db.Column(db.Integer, db.ForeignKey('sitio.id'), unique=True, nullable=True)
    comunidad_id = db.Column(db.Integer, db.ForeignKey('comunidad.id'), unique=True, nullable=True)
    asignaciones_departamento = db.relationship('AsignacionDepartamento', backref='informe', lazy=True)
    anexos_fotograficos = db.relationship('AnexosFotograficos', backref='informe', lazy=True)
    meta_id = db.Column(db.Integer, db.ForeignKey('meta.id'), unique=True, nullable=True)
    obra_a_socializar_id = db.Column(db.Integer, db.ForeignKey('obra_a_socializar.id'), unique=True, nullable=True)

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=True)
    
    asignaciones_departamento = db.relationship('AsignacionDepartamento', backref='departamento', lazy=True)

class AsignacionDepartamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), unique=True, nullable=True)
    informe_id = db.Column(db.Integer, db.ForeignKey('informe.id'), unique=True, nullable=True)

class PDOT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    
    informes = db.relationship('Informe', backref='PDOT', lazy=True)

class ObraASocializar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    
    informe = db.relationship('Informe', backref='obra_a_socializar', uselist=False)

class AnexosFotograficos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firma_respaldo = db.Column(db.String, nullable=False)
    foto = db.Column(db.String, nullable=True)
    
    informe_id = db.Column(db.Integer, db.ForeignKey('informe.id'), unique=True, nullable=True)
