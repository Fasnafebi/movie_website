from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = [
            'title',
            'poster',
            'description',
            'release_date',
            'actors',
            'rating',
            'category',
            'trailer_url'
        ]

        widgets = {
            'release_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'rows': 3
            }),
        }