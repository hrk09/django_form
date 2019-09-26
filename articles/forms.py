from django import forms

# form 쓰는 이유? 사용자가 건네주는 입력값을 form이라는 class가 한번에 받아서 유효성 확인 가능하기 때문에 사용함
# 유효성 확인 후, 검증된 데이터 form에서 가져와서 씀(그냥 raw data를 바로 받아오는 거보다 나음)

# 사용자에게 입력받는 field 만 작성
class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력할 `수` 있어요',
            }
        ),

    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력할 `수` 있어요',
                'rows': 5,
                'cols': 50,
            }
        )
    )
