from django.http import HttpResponse

def home(request):
    return HttpResponse("3D Ecommerce Website")