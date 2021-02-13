from django.shortcuts import render
from .forms import HouseInputForm
from .models import House

# Create your views here.
def main(request):
    return render(request, 'alaboja/main.html')

def myhome(request):
    if request.method == 'POST':
        user = {}
        user['people'] = request.POST['people']
        user['category'] = request.POST['category']
        user['rating'] = request.POST['rating']
        user['income'] = request.POST['income']
        user['gu'] = request.POST['gu']
        user['area'] = request.POST['area']
        
        
    return render(request, 'alaboja/myhome.html')

def aboutus(request):
    return render(request, 'alaboja/aboutus.html')

def address(request):
    return render(request, 'alaboja/address.html')

def store(request):
    if request.method == 'POST':
        form = HouseInputForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Invalid Input")
        csv_input = form.cleaned_data['csv_input'].split('\n')
        header = [ col.strip() for col in csv_input[0].split(',') ]
        lines = csv_input[1:]

        translate = {}
        translate['단지명'] = 'name'
        translate['주소'] = 'address'
        translate['공급유형'] = 'category'
        translate['공급면적'] = 'area'
        translate['세대수'] = 'num'
        translate['가구원수'] = 'people'
        translate['공급대상'] = 'target'
        translate['소득분위'] = 'rating'
        translate['소득/자산'] = 'income'

        for line in lines:
            if line.count(',') != len(header) - 1:
                continue
            options = {}
            for idx, token in enumerate(line.split(',')):
                options[translate[header[idx]]] = token.strip()
            house = House.objects.get_or_create(**options)

    form = HouseInputForm()

    return render(request, 'alaboja/store.html', {
        'form': form,
    })