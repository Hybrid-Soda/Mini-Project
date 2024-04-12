from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs = {'class': 'form-select'}),
            'score': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.5',
                'min': '0',
                'max': '5',
                }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }