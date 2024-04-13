from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
from pyknow import KnowledgeEngine, DefFacts, Rule, Fact, MATCH
from django.db.models import Count
from .models import LugarTuristico, Calificacion

class SistemaExperto(KnowledgeEngine):
    @DefFacts()
    def initial_facts(self):
        yield Fact(action="recomendar_lugares")
        yield Fact(categoria='Ciudad de Arequipa')
        yield Fact(categoria='Alrededores de Arequipa')
        yield Fact(categoria='Pueblos')
        yield Fact(categoria='Playas')
        yield Fact(hay_lugares_categoría=True, categoria='Ciudad de Arequipa')
        yield Fact(cantidad_comentarios=10)
        yield Fact(popularidad_lugar='Alta')
        yield Fact(calificación_alta_disponible=True)
        yield Fact(usuarios_registrados=True)
        yield Fact(hay_lugares_categoría=True, categoria='Alrededores de Arequipa')
        yield Fact(cantidad_lugares=100)
        yield Fact(comentarios_disponibles=True)
        yield Fact(calificaciones_disponibles=True)
        yield Fact(preferencia_lugares_cercanos=True)
        yield Fact(usuarios_registrados=True)
        yield Fact(comentarios_disponibles=True)
        yield Fact(calificaciones_disponibles=True)
        yield Fact(preferencia_lugares_cercanos=True)
        yield Fact(cantidad_lugares=100)
        yield Fact(preferencia_precios_bajos=True)
        yield Fact(preferencia_horarios_amplios=True)
        yield Fact(preferencia_atracciones_cercanas=True)
        yield Fact(preferencia_popularidad_alta=True)
        yield Fact(preferencia_categorias=['Playas', 'Pueblos'])
        yield Fact(preferencia_atracciones_cercanas=True)
        yield Fact(preferencia_popularidad_alta=True)
        yield Fact(preferencia_categorias=['Alrededores de Arequipa', 'Pueblos'])
        yield Fact(preferencia_horarios_amplios=True)
        yield Fact(preferencia_precios_bajos=True)
        yield Fact(preferencia_accesibilidad=True)
        yield Fact(preferencia_naturaleza=True)
        yield Fact(preferencia_historia=True)
        yield Fact(preferencia_gastronomia=True)
        yield Fact(preferencia_aventura=True)
        yield Fact(fotos_disponibles=True)
        yield Fact(cantidad_atracciones_cercanas=3)
        yield Fact(guias_turisticos_disponibles=True)
        yield Fact(acceso_transporte_publico=True)
        yield Fact(estacionamiento_disponible=True)

    #regla 1
    @Rule(Fact(action='recomendar_lugares'), Fact(usuarios_registrados=True))
    def recomendar_usuarios_registrados(self):
        print("Ejecutando regla: recomendar_usuarios_registrados")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a la existencia de usuarios registrados: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a la existencia de usuarios registrados.'))

    #regla 2
    @Rule(Fact(action='recomendar_lugares'), Fact(comentarios_disponibles=True))
    def recomendar_por_comentarios(self):
        print("Ejecutando regla: recomendar_por_comentarios")
        lugares = LugarTuristico.objects.filter(comentario__isnull=False).distinct()
        for lugar in lugares:
            print(f"Recomendando lugar con comentarios disponibles: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene comentarios disponibles.'))

    #regla 3
    @Rule(Fact(action='recomendar_lugares'), Fact(categoria='Ciudad de Arequipa'))
    def recomendar_lugares_en_ciudad(self):
        print("Ejecutando regla: recomendar_lugares_en_ciudad")
        lugares = LugarTuristico.objects.filter(categoria__nombre='Ciudad de Arequipa')
        for lugar in lugares:
            print(f"Recomendando lugar en la categoría: Ciudad de Arequipa: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" en la ciudad de Arequipa.'))

    #regla 4
    @Rule(Fact(action='recomendar_lugares'), Fact(categoria='Alrededores de Arequipa'))
    def recomendar_lugares_en_alrededores(self):
        print("Ejecutando regla: recomendar_lugares_en_alrededores")
        lugares = LugarTuristico.objects.filter(categoria__nombre='Alrededores de Arequipa')
        for lugar in lugares:
            print(f"Recomendando lugar en los alrededores de Arequipa: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" en los alrededores de Arequipa.'))

    #regla 5
    @Rule(Fact(action='recomendar_lugares'), Fact(categoria='Pueblos'))
    def recomendar_lugares_en_pueblos(self):
        print("Ejecutando regla: recomendar_lugares_en_pueblos")
        lugares = LugarTuristico.objects.filter(categoria__nombre='Pueblos')
        for lugar in lugares:
            print(f"Recomendando lugar en la categoría: Pueblos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" en pueblos.'))

    #regla 6
    @Rule(Fact(action='recomendar_lugares'), Fact(categoria='Playas'))
    def recomendar_lugares_en_playas(self):
        print("Ejecutando regla: recomendar_lugares_en_playas")
        lugares = LugarTuristico.objects.filter(categoria__nombre='Playas')
        for lugar in lugares:
            print(f"Recomendando lugar en la categoría: Playas: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" en playas.'))

    #regla 7
    @Rule(Fact(action='recomendar_lugares'), Fact(calificaciones_disponibles=True))
    def recomendar_por_calificaciones(self):
        print("Ejecutando regla: recomendar_por_calificaciones")
        lugares = LugarTuristico.objects.annotate(avg_rating=Avg('calificacion__puntuacion')).filter(avg_rating__gte=4)
        for lugar in lugares:
            print(f"Recomendando lugar con calificaciones altas disponibles: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene calificaciones altas disponibles.'))
    
    #regla 8
    @Rule(Fact(action='recomendar_lugares'), Fact(cantidad_comentarios=10))
    def recomendar_por_cantidad_comentarios(self):
        print("Ejecutando regla: recomendar_por_cantidad_comentarios")
        lugares = LugarTuristico.objects.annotate(num_comentarios=Count('comentario')).filter(num_comentarios__gte=10)
        for lugar in lugares:
            print(f"Recomendando lugar con al menos 10 comentarios: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene al menos 10 comentarios.'))

    #regla 9
    @Rule(Fact(action='recomendar_lugares'), Fact(hay_lugares_categoría=True, categoria='Ciudad de Arequipa'))
    def recomendar_lugares_en_ciudad(self):
        print("Ejecutando regla: recomendar_lugares_en_ciudad")
        lugares = LugarTuristico.objects.filter(categoria__nombre='Ciudad de Arequipa')
        for lugar in lugares:
            print(f"Recomendando lugar en la categoria: Ciudad de Arequipa: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" en la ciudad de Arequipa.'))

    #regla 10
    @Rule(Fact(action='recomendar_lugares'), Fact(hay_lugares_categoría=True, categoria='Alrededores de Arequipa'))
    def recomendar_lugares_en_alrededores(self):
        print("Ejecutando regla: recomendar_lugares_en_alrededores")
        lugares = LugarTuristico.objects.filter(categoria__nombre='Alrededores de Arequipa')
        for lugar in lugares:
            print(f"Recomendando lugar en los alrededores de Arequipa: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" en los alrededores de Arequipa.'))

    #regla 11
    @Rule(Fact(action='recomendar_lugares'), Fact(cantidad_lugares=100))
    def recomendar_por_cantidad_lugares(self):
        print("Ejecutando regla: recomendar_por_cantidad_lugares")
        lugares = LugarTuristico.objects.all()[:100]
        for lugar in lugares:
            print(f"Recomendando lugar debido a la cantidad de lugares disponibles: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a que hay una amplia selección disponible.'))

    #regla 12
    @Rule(Fact(action='recomendar_lugares'), Fact(popularidad_lugar='Alta'))
    def recomendar_populares(self):
        print("Ejecutando regla: recomendar_populares")
        lugares = LugarTuristico.objects.filter(popularidad='Alta')
        for lugar in lugares:
            print(f"Recomendando lugar popular: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque es popular y concurrido.'))

    #regla 13
    @Rule(Fact(action='recomendar_lugares'), Fact(calificación_alta_disponible=True))
    def recomendar_calificacion_alta(self):
        print("Ejecutando regla: recomendar_calificacion_alta")
        lugares = LugarTuristico.objects.annotate(avg_rating=Avg('calificacion__puntuacion')).filter(avg_rating__gte=4)
        for lugar in lugares:
            print(f"Recomendando lugar con calificaciones altas disponibles: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene calificaciones altas disponibles.'))

    #regla 14
    @Rule(Fact(action='recomendar_lugares'), Fact(usuarios_registrados=True))
    def recomendar_usuarios_registrados(self):
        print("Ejecutando regla: recomendar_usuarios_registrados")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a la existencia de usuarios registrados: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a la existencia de usuarios registrados.'))

    #regla 15
    @Rule(Fact(action='recomendar_lugares'), Fact(horario_funcionamiento=True))
    def recomendar_por_horario(self):
        print("Ejecutando regla: recomendar_por_horario")
        lugares = LugarTuristico.objects.filter(horario_funcionamiento__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene un horario de funcionamiento definido: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene un horario de funcionamiento definido.'))

    #regla 16
    @Rule(Fact(action='recomendar_lugares'), Fact(precio_entrada=True))
    def recomendar_por_precio_entrada(self):
        print("Ejecutando regla: recomendar_por_precio_entrada")
        lugares = LugarTuristico.objects.filter(precio_entrada__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene precio de entrada disponible: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene precio de entrada disponible.'))

    #regla 17
    @Rule(Fact(action='recomendar_lugares'), Fact(sitio_web=True))
    def recomendar_por_sitio_web(self):
        print("Ejecutando regla: recomendar_por_sitio_web")
        lugares = LugarTuristico.objects.filter(sitio_web__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene un sitio web disponible: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene un sitio web disponible.'))

    #regla 18
    @Rule(Fact(action='recomendar_lugares'), Fact(telefono_contacto=True))
    def recomendar_por_telefono_contacto(self):
        print("Ejecutando regla: recomendar_por_telefono_contacto")
        lugares = LugarTuristico.objects.filter(telefono_contacto__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene un teléfono de contacto disponible: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene un teléfono de contacto disponible.'))

    #regla 19
    @Rule(Fact(action='recomendar_lugares'), Fact(latitud=True), Fact(longitud=True))
    def recomendar_por_coordenadas_geograficas(self):
        print("Ejecutando regla: recomendar_por_coordenadas_geograficas")
        lugares = LugarTuristico.objects.filter(latitud__isnull=False, longitud__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene coordenadas geográficas definidas: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene coordenadas geográficas definidas.'))

    #regla 20
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_lugares_cercanos=True))
    def recomendar_por_lugares_cercanos(self):
        print("Ejecutando regla: recomendar_por_lugares_cercanos")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a que está cerca de otros lugares preferidos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a que está cerca de otros lugares preferidos.'))

    #regla 21
    @Rule(Fact(action='recomendar_lugares'), Fact(horario_funcionamiento=True), Fact(precio_entrada=True))
    def recomendar_por_horario_y_precio(self):
        print("Ejecutando regla: recomendar_por_horario_y_precio")
        lugares = LugarTuristico.objects.filter(horario_funcionamiento__isnull=False, precio_entrada__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene horario de funcionamiento y precio de entrada definidos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene horario de funcionamiento y precio de entrada definidos.'))

    #regla 22
    @Rule(Fact(action='recomendar_lugares'), Fact(horario_funcionamiento=True), Fact(sitio_web=True))
    def recomendar_por_horario_y_sitio_web(self):
        print("Ejecutando regla: recomendar_por_horario_y_sitio_web")
        lugares = LugarTuristico.objects.filter(horario_funcionamiento__isnull=False, sitio_web__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene horario de funcionamiento y sitio web definidos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene horario de funcionamiento y sitio web definidos.'))

    #regla 23
    @Rule(Fact(action='recomendar_lugares'), Fact(precio_entrada=True), Fact(telefono_contacto=True))
    def recomendar_por_precio_entrada_y_telefono(self):
        print("Ejecutando regla: recomendar_por_precio_entrada_y_telefono")
        lugares = LugarTuristico.objects.filter(precio_entrada__isnull=False, telefono_contacto__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene precio de entrada y teléfono de contacto definidos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene precio de entrada y teléfono de contacto definidos.'))

    #regla 24
    @Rule(Fact(action='recomendar_lugares'), Fact(latitud=True), Fact(longitud=True), Fact(preferencia_lugares_cercanos=True))
    def recomendar_por_coordenadas_y_lugares_cercanos(self):
        print("Ejecutando regla: recomendar_por_coordenadas_y_lugares_cercanos")
        lugares = LugarTuristico.objects.filter(latitud__isnull=False, longitud__isnull=False)  # Filtra según tus criterios específicos
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene coordenadas geográficas definidas y está cerca de otros lugares preferidos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a que tiene coordenadas geográficas definidas y está cerca de otros lugares preferidos.'))

    #regla 25
    @Rule(Fact(action='recomendar_lugares'), Fact(telefono_contacto=True), Fact(sitio_web=True))
    def recomendar_por_telefono_y_sitio_web(self):
        print("Ejecutando regla: recomendar_por_telefono_y_sitio_web")
        lugares = LugarTuristico.objects.filter(telefono_contacto__isnull=False, sitio_web__isnull=False)
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene teléfono de contacto y sitio web definidos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene teléfono de contacto y sitio web definidos.'))

    #regla 26
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_atracciones_cercanas=True))
    def recomendar_por_atracciones_cercanas(self):
        print("Ejecutando regla: recomendar_por_atracciones_cercanas")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a que tiene atracciones cercanas: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a que tiene atracciones cercanas.'))

    #regla 27
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_popularidad_alta=True))
    def recomendar_por_popularidad_alta(self):
        print("Ejecutando regla: recomendar_por_popularidad_alta")
        lugares = LugarTuristico.objects.filter(popularidad='Alta')
        for lugar in lugares:
            print(f"Recomendando lugar porque es popular y concurrido: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque es popular y concurrido.'))

    #regla 28
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_categorias=['Playas', 'Pueblos']))
    def recomendar_por_preferencia_categorias(self):
        print("Ejecutando regla: recomendar_por_preferencia_categorias")
        lugares = LugarTuristico.objects.filter(categoria__nombre__in=['Playas', 'Pueblos'])
        for lugar in lugares:
            print(f"Recomendando lugar porque pertenece a las categorías preferidas: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque pertenece a las categorías preferidas.'))

    #regla 29
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_horarios_amplios=True))
    def recomendar_por_horarios_amplios(self):
        print("Ejecutando regla: recomendar_por_horarios_amplios")
        lugares = LugarTuristico.objects.filter(horarios_amplios=True)
        for lugar in lugares:
            print(f"Recomendando lugar porque tiene horarios amplios de funcionamiento: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene horarios amplios de funcionamiento.'))

    #regla 30
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_precios_bajos=True))
    def recomendar_por_precios_bajos(self):
        print("Ejecutando regla: recomendar_por_precios_bajos")
        lugares = LugarTuristico.objects.filter(precios_bajos=True)
        for lugar in lugares:
            print(f"Recomendando lugar porque tiene precios bajos de entrada: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" porque tiene precios bajos de entrada.'))

    #regla 31
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_accesibilidad=True))
    def recomendar_por_accesibilidad(self):
        print("Ejecutando regla: recomendar_por_accesibilidad")
        lugares = LugarTuristico.objects.filter(accesibilidad=True)
        for lugar in lugares:
            print(f"Recomendando lugar por su accesibilidad: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" por su accesibilidad.'))

    #regla 32
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_naturaleza=True))
    def recomendar_por_naturaleza(self):
        print("Ejecutando regla: recomendar_por_naturaleza")
        lugares = LugarTuristico.objects.filter(naturaleza=True)
        for lugar in lugares:
            print(f"Recomendando lugar por su entorno natural: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" por su entorno natural.'))

    #regla 33
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_historia=True))
    def recomendar_por_historia(self):
        print("Ejecutando regla: recomendar_por_historia")
        lugares = LugarTuristico.objects.filter(historia=True)
        for lugar in lugares:
            print(f"Recomendando lugar por su importancia histórica: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" por su importancia histórica.'))

    #regla 34
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_gastronomia=True))
    def recomendar_por_gastronomia(self):
        print("Ejecutando regla: recomendar_por_gastronomia")
        lugares = LugarTuristico.objects.filter(gastronomia=True)
        for lugar in lugares:
            print(f"Recomendando lugar por su oferta gastronómica: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" por su oferta gastronómica.'))

    #regla 35
    @Rule(Fact(action='recomendar_lugares'), Fact(preferencia_aventura=True))
    def recomendar_por_aventura(self):
        print("Ejecutando regla: recomendar_por_aventura")
        lugares = LugarTuristico.objects.filter(aventura=True)
        for lugar in lugares:
            print(f"Recomendando lugar por sus actividades de aventura: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" por sus actividades de aventura.'))

    #regla 36
    @Rule(Fact(action='recomendar_lugares'), Fact(fotos_disponibles=True))
    def recomendar_por_fotos_disponibles(self):
        print("Ejecutando regla: recomendar_por_fotos_disponibles")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a la disponibilidad de fotos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a la disponibilidad de fotos.'))
    
    #regla 37
    @Rule(Fact(action='recomendar_lugares'), Fact(cantidad_atracciones_cercanas=MATCH.num))
    def recomendar_por_atracciones_cercanas(self, num):
        print("Ejecutando regla: recomendar_por_atracciones_cercanas")
        if num >= 3:
            lugares = LugarTuristico.objects.all()
            for lugar in lugares:
                print(f"Recomendando lugar debido a la cantidad de atracciones cercanas: {lugar.nombre}")
                self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a la cantidad de atracciones cercanas.'))

    #regla 38
    @Rule(Fact(action='recomendar_lugares'), Fact(guias_turisticos_disponibles=True))
    def recomendar_por_guias_turisticos(self):
        print("Ejecutando regla: recomendar_por_guias_turisticos")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a la disponibilidad de guías turísticos: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a la disponibilidad de guías turísticos.'))

    #regla 39
    @Rule(Fact(action='recomendar_lugares'), Fact(acceso_transporte_publico=True))
    def recomendar_por_acceso_transporte_publico(self):
        print("Ejecutando regla: recomendar_por_acceso_transporte_publico")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido al acceso al transporte público: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido al acceso al transporte público.'))

    #regla 40
    @Rule(Fact(action='recomendar_lugares'), Fact(estacionamiento_disponible=True))
    def recomendar_por_estacionamiento_disponible(self):
        print("Ejecutando regla: recomendar_por_estacionamiento_disponible")
        lugares = LugarTuristico.objects.all()
        for lugar in lugares:
            print(f"Recomendando lugar debido a la disponibilidad de estacionamiento: {lugar.nombre}")
            self.declare(Fact(recomendacion_hecha=True, recomendacion=f'Puedo recomendar el lugar turístico "{lugar.nombre}" debido a la disponibilidad de estacionamiento.'))


def lugares_con_calificaciones_json(request):
    # Instanciamos el motor de reglas
    engine = SistemaExperto()
    # Ejecutamos el motor de reglas
    engine.reset()
    engine.run()
    # Filtrar los lugares con una puntuación promedio mayor que 4
    lugares = LugarTuristico.objects.annotate(promedio_calificaciones=Avg('calificacion__puntuacion')).filter(promedio_calificaciones__gt=2)
    # Crear una lista para almacenar los datos de los lugares turísticos
    lugares_con_promedio = []
    # Iterar sobre cada lugar turístico y obtener su información
    for lugar in lugares:
        # Crear un diccionario con la información del lugar turístico
        lugar_data = {
            'nombre': lugar.nombre,
            'ubicacion': lugar.ubicacion,
            'categoria': lugar.categoria.nombre,
            'promedio_calificaciones': round(lugar.promedio_calificaciones, 1),
            'imagen_url': f"/static/img/{lugar.id}.png"
        }
        
        # Agregar los datos del lugar turístico a la lista
        lugares_con_promedio.append(lugar_data)
    # Devolver los datos en formato JSON
    return JsonResponse(lugares_con_promedio, safe=False)


def lugares_con_calificaciones_html(request):
    return render(request, 'lugares_con_calificaciones.html')


'''
def lugares_con_calificaciones_json(request):
    # Obtener todos los lugares turísticos
    lugares = LugarTuristico.objects.all()

    # Crear una lista para almacenar los datos de los lugares turísticos
    lugares_con_promedio = []

    # Iterar sobre cada lugar turístico y obtener su información
    for lugar in lugares:
        # Obtener la puntuación promedio del lugar turístico
        promedio_calificaciones = Calificacion.objects.filter(lugar=lugar).aggregate(promedio=Avg('puntuacion'))['promedio']
        
        # Verificar si se obtuvo un promedio de calificaciones
        if promedio_calificaciones is not None:
            # Crear un diccionario con la información del lugar turístico
            lugar_data = {
                'nombre': lugar.nombre,
                'ubicacion': lugar.ubicacion,
                'categoria': lugar.categoria.nombre,
                'promedio_calificaciones': round(promedio_calificaciones, 1),
                'imagen_url': f"/static/img/{lugar.id}.png"  # Ruta de la imagen
            }
            
            # Agregar los datos del lugar turístico a la lista
            lugares_con_promedio.append(lugar_data)

    # Devolver los datos en formato JSON
    return JsonResponse(lugares_con_promedio, safe=False)
'''