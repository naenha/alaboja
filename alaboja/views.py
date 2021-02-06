from django.shortcuts import render
from .forms import HouseInputForm

# Create your views here.
def main(request):
    return render(request, 'alaboja/main.html')

def myhome(request):
    return render(request, 'alaboja/myhome.html')

def aboutus(request):
    return render(request, 'alaboja/aboutus.html')

def store(request):
    if request.method == 'POST':
        form = HouseInputForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Invalid Input")
        csv_input = form.cleaned_data['csv_input'].split('\n')

    form = HouseInputForm()
    
    return render(request, 'alaboja/store.html', {
        'form': form,
    })