from django.http import HttpResponse


#Saludo inicial
def index(request):
    return HttpResponse("Holi")


