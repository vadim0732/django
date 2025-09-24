from django.shortcuts import render, HttpResponse

def hello(request):
    text = "Lorem ipsum"
    return render(request, 'main.html', {'my_note': text})


