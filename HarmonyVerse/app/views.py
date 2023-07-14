from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def audio(request):
    return render(request,'audio.html')
def artist(request):
    return render(request,'artist.html')
def playlist(request):
    return render(request,'playlist.html')
def search(request):
    return render(request,'searchartists.html')
def album(request):
    return render(request,'album.html')
def about(request):
    return render(request,'about.html')