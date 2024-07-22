from django import forms
from .models import BF_Post


class PostForm(forms.ModelForm):
    class Meta:
        model = BF_Post
        fields = ['author','title','content','categories','tags']