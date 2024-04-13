from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class LugarTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    popularidad = models.CharField(max_length=50, choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja')
    horario_funcionamiento = models.CharField(max_length=200, blank=True, null=True)
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sitio_web = models.URLField(max_length=200, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    atracciones_cercanas = models.BooleanField(default=False)
    horarios_amplios = models.BooleanField(default=False)
    precios_bajos = models.BooleanField(default=False)
    accesibilidad = models.BooleanField(default=False)
    naturaleza = models.BooleanField(default=False)
    historia = models.BooleanField(default=False)
    gastronomia = models.BooleanField(default=False)
    aventura = models.BooleanField(default=False)
    fotos_disponibles = models.BooleanField(default=False)
    cantidad_atracciones_cercanas = models.IntegerField(default=0)
    guias_turisticos_disponibles = models.BooleanField(default=False)
    acceso_transporte_publico = models.BooleanField(default=False)
    estacionamiento_disponible = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    lugar = models.ForeignKey(LugarTuristico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Calificacion(models.Model):
    lugar = models.ForeignKey(LugarTuristico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha = models.DateTimeField(auto_now_add=True)
