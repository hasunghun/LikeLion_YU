from django import forms
from .models import Post, Comment    # 모델 기반(ModelForm)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'   # models.py의 전체 field를 입력 받음
        # fields = ['title', 'body'] 특정 field만 입력 받음

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
