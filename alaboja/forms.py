from django import forms

class HouseInputForm(forms.Form):
    tsv_input = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': """
TSV 파일 내용을 입력해주세요.

단지명	주소	위도	경도	공급유형	공급면적	세대수	가구원수	공급대상	소득분위	소득/자산
예)
매입다가구(서울종로구)	서울특별시 종로구 대학로5가길	37.5786552	127.0014516	기존주택매입임대	27.17	1	1-7	수급자	1	50%이하
            """
        }
    ))