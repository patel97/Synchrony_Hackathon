from django.shortcuts import render

def test(request):
    print(request.POST)
    