from django.shortcuts import render

# Create your views here.
def dashboard(request):
    # if request.user.is_authenticated():
    return render(request,'index.html')