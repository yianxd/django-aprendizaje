from django.http import request,HttpResponse
from django.template import Template,Context
import datetime

def primero(request):
    doc_e=open("C:/Users/Aprendiz/Pictures/prueba/proyecto/proyecto/pantillas/primera.html")
    #doc_e=open("./proyecto/pantillas/primera.html")
    plt=Template(doc_e.read())
    doc_e.close()
    ctx=Context()
    doc=plt.render(ctx)
    return HttpResponse(doc)


def segundo(request):

    class Persona:
        def __init__(self,nombre,documento):
            self.nombre=nombre
            self.documento=documento

        def getNombre(self):
            return self.nombre



    nombre='juan'
    obj1=Persona(nombre,12334)

    tiempo=datetime.datetime.now()
    doc_e=open("C:/Users/Aprendiz/Pictures/prueba/proyecto/proyecto/pantillas/segundo.html")
    #doc_e=open("./proyecto/pantillas/primera.html")
    plt=Template(doc_e.read())
    doc_e.close()
    ctx=Context({   'nombre':nombre,
                    'tiempo':tiempo,
                    'clase':obj1})
    doc=plt.render(ctx)
    return HttpResponse(doc)