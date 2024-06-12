from django import forms

from ch04_models.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
        ]