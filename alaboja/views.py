from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'alaboja/main.html')

def myhome(request):
    return render(request, 'alaboja/myhome.html')

def aboutus(request):
    return render(request, 'alaboja/aboutus.html')