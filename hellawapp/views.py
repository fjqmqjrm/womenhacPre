from django.shortcuts import render
def hellaw_main(request):
    return render(request, 'hellawapp/mainPage.html', {})

def login(request):
    return render(request, 'hellawapp/login.html', {})