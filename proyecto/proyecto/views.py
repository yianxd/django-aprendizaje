from django.http import request,HttpResponse
from django.template import Template,Context

def primero(request):
    doc_e=open("C:/Users/Aprendiz/Pictures/prueba/proyecto/proyecto/pantillas/primera.html")
    #doc_e=open("./proyecto/pantillas/primera.html")
    plt=Template(doc_e.read())
    doc_e.close()
    ctx=Context()
    doc=plt.render(ctx)
    return HttpResponse(doc)


def segundo(request):

    nombre='juan'
    doc_e=open("C:/Users/Aprendiz/Pictures/prueba/proyecto/proyecto/pantillas/segundo.html")
    #doc_e=open("./proyecto/pantillas/primera.html")
    plt=Template(doc_e.read())
    doc_e.close()
    ctx=Context({'nombre':nombre})
    doc=plt.render(ctx)
    return HttpResponse(doc)