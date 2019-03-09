import requests
from django.shortcuts import render


        
def index_page(request):
        context = {
        }
        return render(request, 'index.html', context)
        
        


def projects_page(request):

        context = {
        }
        return render(request, 'projects.html', context)
        
        
        
def contact_page(request):

        context = {
        }
        return render(request, 'contact.html', context)

def github_page(request):

        context = {
        }
        return render(request, 'github.html', context)





def github_page(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/stevezlin/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

