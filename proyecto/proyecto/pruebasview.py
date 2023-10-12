from django.http import request,HttpResponse
import datetime


def prueba(request):
    return HttpResponse('hola')


def hmtl(request):
    return HttpResponse('<html><body><h1>El Descanso Es Mas Temprano</h1></body></html>')


a = '<html><body><h1>Prueba html en variables</h1></body></html>'

def variable(request):
    return HttpResponse(a)

def hora(request):
    fecha=datetime.datetime.now()

    doc="""
    <body>
    <h1>
    Fecha y hora %s
    </h1>
    </body>
    </html>""" %fecha

    return HttpResponse(doc)


def edad(request,edad,a,aF):
    edadA=edad
    añoA=a
    periodo=aF-a
    edadFutura=periodo+edad
    doc="""<html>
            <body>
            <h1>Su edad es %s y en el año %s tendras %s</h1>
            <body>
            </html>""" %(edadA,añoA,edadFutura)
    return HttpResponse(doc)

