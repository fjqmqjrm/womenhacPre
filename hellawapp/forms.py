from django import forms
from .models import Board
class BoardForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': ''}))

    class Meta:
        model = Board
        fields = ('title', 'description')

