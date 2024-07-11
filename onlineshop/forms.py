from django import forms
from .models import Post, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']


PostImageFormSet = forms.inlineformset_factory(Post, PostImage, form=PostImageForm, extra=3)
