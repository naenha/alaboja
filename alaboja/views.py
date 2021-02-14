from django.shortcuts import render
from .forms import HouseInputForm
from .models import House

# Create your views here.
def main(request):
    return render(request, 'alaboja/main.html')

def myhome(request):
    def money(house):
        if house.category == "영구임대":
            return "시중 시세의 30% 수준(평균 보증금 190만원 임대료 4만 5,000원)"
        elif house.category == "국민임대":
            return "시중 전세 시세의 60%~80% 수준(평균 보증금 3,700만원 임대료 28만원)"
        elif house.category == "행복주택":
            return "시중 시세의 60%~80% 수준"
        elif house.category == "장기전세":
            return "주변 전세 시세의 80% 이하 수준"
        elif ("집주인" in house.category) or ("장기임대" in house.category):
            return "시중 시세의 70~85% 수준"
        elif "공공임대" in house.category:
            return "시중 전세 시세의 90% 수준(평균 보증금 46,688,535원 임대료 597,000원)"
        elif house.category == "기존주택매입임대":
            return "시중 전세 시세의 30% 수준(평균 보증금 1,800만원 임대료 19만원)"
        else:
            return "시중 전세 시세의 90% 수준"
    recommend_list = {}
    if request.method == 'POST':
        user = {}
        user['people'] = request.POST['people']#가구원수
        user['category'] = request.POST['category']#공급유형
        user['rating'] = request.POST['rating']#소득분위
        user['income'] = request.POST['income']#소득/자산
        user['gu'] = request.POST['gu']#행정구
        user['area'] = request.POST['area']#희망전용면적

        house_list = []
        max_count = 0
        for house in House.objects.all():
            must = 0; count = 0
            #가구원수
            if int(house.people.split('-')[0]) <= int(user['people']) <= int(house.people.split('-')[-1]):
                count+=1
            #공급유형
            target = house.target.strip()
            if house.target[0]=="\"": target = house.target[1:-1]
            if (target == "전체") or (user['category'] in target.split(',')):
                count+=1; must+=1
            # 소득분위
            rating = house.rating.strip()
            if "-" in rating:
                rating = list(range(int(rating.split('-')[0]), int(rating.split('-')[-1])+1))
            if (rating == "조건없음") or (user['rating'] in rating):
                count+=1; must+=1
            #소득/자산
            income = house.income
            if "\"" in income: income = income[1:-1]
            if "조건" in income: 
                count+=1; must+=1
            elif (income == "신청자:80%이하, 세대원:100%이하") and (int(user['income']) <= 80):
                count+=1; must+=1
            elif int(user['income']) <= int(income.split("%")[0].strip()):
                count+=1; must+=1
            #행정구
            if user['gu'] == house.address.split()[1]: count+=1
            #희망전용면적
            if (user['area']=="40") and house.area<40: count+=1
            elif (user['area']=="40-60") and house.area<60: count+=1
            elif (user['area']=="60-85") and house.area<85: count+=1
            elif (user['area']=="85") and house.area>85: count+=1

            if count>max_count: max_count = count
            if must == 3: house_list.append([house, count])

        #추천주택의 개수가 0인 경우, 공공임대(50년) 주택 추천
        if len(house_list) == 0:
            for house in House.objects.all():
                if house.category == "공공임대(50년)":
                    recommend_list[house] = "시중 전세 시세의 90% 수준"
        #사용자의 조건에 가장 많이 부합하는 조건을 갖는 주택 추천
        else:
            temp = {}
            for house, count in house_list:
                target = house.target.strip()
                if house.target[0]=="\"": target = house.target[1:-1]
                if (count==max_count):
                    if user['category'] in target.split(','):
                        recommend_list[house] = money(house)
                    else:
                        temp[house] = money(house)
            if len(recommend_list)==0: recommend_list = temp
            
    return render(request, 'alaboja/myhome.html', recommend_list)

def aboutus(request):
    return render(request, 'alaboja/aboutus.html')

def address(request):
    return render(request, 'alaboja/address.html')

def store(request):
    if request.method == 'POST':
        form = HouseInputForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Invalid Input")
        tsv_input = form.cleaned_data['tsv_input'].split('\n')
        header = [ col.strip() for col in tsv_input[0].split('\t') ]
        lines = tsv_input[1:]

        translate = {}
        translate['단지명'] = 'name'
        translate['주소'] = 'address'
        translate['위도'] = 'latitude'
        translate['경도'] = 'longitude'
        translate['공급유형'] = 'category'
        translate['공급면적'] = 'area'
        translate['세대수'] = 'num'
        translate['가구원수'] = 'people'
        translate['공급대상'] = 'target'
        translate['소득분위'] = 'rating'
        translate['소득/자산'] = 'income'

        for line in lines:
            if line.count('\t') != len(header) - 1:
                continue
            options = {}
            for idx, token in enumerate(line.split('\t')):
                options[translate[header[idx]]] = token.strip()
            house = House.objects.get_or_create(**options)

    form = HouseInputForm()

    return render(request, 'alaboja/store.html', {
        'form': form,
    })