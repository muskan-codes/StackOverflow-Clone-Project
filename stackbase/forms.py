from .models import Comment
from django import forms 

#created to pass Commentform in views.py
class CommentForm(forms.ModelForm): #define class Commentform and set forms.model in it
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }