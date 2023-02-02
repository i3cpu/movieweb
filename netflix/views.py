import requests
from django.shortcuts import render
import wikipedia


def wiki(text):
    return wikipedia.summary(text)

# Create your views here.

def main(request):
    return render(request, 'netflix/main.html') 

def movie(request):
    try:

        a=request.GET.get('movie')
        url = f"https://pixabay.com/api/?key=31500342-4487139e4fe815dfbb649cc04&q={a}&image_type=photo"
        response = requests.request("GET", url).json()
        w=wikipedia.summary(a)
        data = {
                'photo': list(response.get('hits'))[0].get("largeImageURL"),
                'b':a,
                'w':w
                
        }
        return render(request, 'netflix/movie.html',data)
    except :
        return render(request, 'netflix/movie.html',{'a':"В базе нет такого или проверьте соединение", 'b':a})