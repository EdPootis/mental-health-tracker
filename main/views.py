from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306208363',
        'name': 'Edmond Christian',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
