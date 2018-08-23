# 이 파일의 이름은 다른 이름이 되어도 상관없음(가급적이면 네임을 지켜주기 바람)

from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text'] # ()같은 튜플보다는 [] 리스트를 사용하는 것이 좋다
        