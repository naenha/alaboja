from django import forms

class HouseInputForm(forms.Form):
    csv_input = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': """
CSV 파일 내용을 입력해주세요.

단지명, 주소, 공급유형, 공급면적, 세대수, 가구원수, 공급대상, 소득분위, 소득/자산
예)
매입다가구(서울종로구), 서울특별시 종로구 대학로5가길, 기존주택매입임대, 27.17, 1, 01-07, 수급자, 1, 50%이하
            """
        }
    ))