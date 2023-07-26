from django.shortcuts import render
import requests
import json
headers={
    'Content-Type':'application/json',
    'Authorization': 'Bearer BQCzkfeliTqn9Sp-pzOE_BSkPytppAe3RSfW9TpGdqfWKizKnYPB-VIUIVfFSCtT2W3O0ulUYnnBxl-ouRmZ3tozZRvhbn-EZSCFVOmh66HPFyjGQtY'
}
# Create your views here.
def home(request):
    new=requests.get("https://api.spotify.com/v1/browse/new-releases?limit=3", headers=headers)
    featured=requests.get("https://api.spotify.com/v1/browse/featured-playlists?limit=6&country=IN",headers=headers)
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


def artist(request,id):
    featured=requests.get(f'https://api.spotify.com/v1/artists/{id}/top-tracks?market=IN', headers=headers)
    status_code=featured.status_code
    featured=featured.json()
    if status_code==200:
        image=featured['tracks'][0]['album']['images'][0]['url']
        return render(request,'artist.html',{"featured":featured['tracks'],"image":image})
    else:
        return render(request,'error.html',{"featured":featured,"message":featured['error']['message']})


def playlist(request,id):
    featured = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    status_code=featured.status_code
    featured=featured.json()
    if status_code==200:
        return render(request, 'playlist.html', {"featured":featured})
    else:
        return render(request, 'error.html', {"featured": featured,"message":featured['error']['message']})
    
    
def search(request):
    symbol=request.GET.get("search")
    featured=requests.get(f'https://api.spotify.com/v1/search?q={symbol}&type=artist', headers=headers)
    status_code=featured.status_code
    featured=featured.json()
    if status_code==200:
        return render(request,'searchartists.html',{"featured":featured['artists']['items']})
    else:
        return render(request,'error.html',{"message":featured['error']['message']})


def album(request,id):
    new=requests.get(f'https://api.spotify.com/v1/albums/{id}',headers=headers)
    status_code=new.status_code
    new = new.json()
    if status_code==200:
        return render(request,'album.html',{"new":new})
    else:
        return render(request,'error.html',{"new":new,"message": new['error']['message']})


def about(request):
    return render(request,'about.html')