from django.shortcuts import render
import requests
import json
headers={
    'Content-Type':'application/json',
    'Authorization': 'Bearer BQDSFdBQ7ReCvTGLF7PwgGeYC5Sxu5Er0AVWX2Cp_NW8sSmByNl5PhkpZG2Y3EgdVP0IhNkc1XgNx6W5CXyIKaAJHS-ay2Hwr5IcZXrx8WrLM68OZfc'
}
# Create your views here.
def home(request):
    new=requests.get("https://api.spotify.com/v1/browse/new-releases?limit=3", headers=headers)
    featured=requests.get("https://api.spotify.com/v1/browse/featured-playlists?limit=3",headers=headers)
    status_code=new.status_code
    new=new.json()
    featured=featured.json()
    if status_code==200:
        new=new['albums']['items']
        featured=featured['playlists']['items']
        return render(request,'home.html',{"new":new,"featured":featured})
    else:
        return render(request,'home.html',{"new":new,"message":new['error']['message']})
    
def audio(request):
    return render(request,'audio.html')
def artist(request):
    return render(request,'artist.html')
def playlist(request):
    data = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    status_code=data.status_code
    data=data.json()
    if status_code==200:
        return render(request, 'music_world/playlist.html', {"data":data})
    else:
        return render(request, 'music_world/error.html', {
            "data": data,"message":data['error']['message']})
def search(request):
    return render(request,'searchartists.html')
def album(request):
    return render(request,'album.html')
def about(request):
    return render(request,'about.html')