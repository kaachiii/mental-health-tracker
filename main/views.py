from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306227955',
        'name': 'Ischika Afrilla',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)