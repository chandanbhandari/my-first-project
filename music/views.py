from django.http import HttpResponse

def index(request):
    return HttpResponse("this is the music app homepage")

def detail(request,album_id):
    return HttpResponse("Details for album id: "+str(album_id))
