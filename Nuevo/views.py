from django.http import HttpResponse
from django.template import Template, Context


def hola(request):
    doc_externo=open("C:/Nuevo/Nuevo/template/index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    
    
    return HttpResponse(documento)