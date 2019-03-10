import requests
from django.shortcuts import render


       # home page
def index_page(request):
        context = {
        }
        return render(request, 'index.html', context)
        
        

        # My Projects page
def projects_page(request):
        
        context = {
        }
        return render(request, 'projects.html', context)
        
        
        # About me
def contact_page(request):

        context = {
        }
        return render(request, 'contact.html', context)




    # My github repos

def github_page(request):

    response = requests.get('https://api.github.com/users/stevezlin/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

