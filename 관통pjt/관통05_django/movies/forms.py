from django import forms
from django.forms import widgets
from .models import Movie, Comment

class MovieForm(forms.ModelForm):  
    genre = forms.ChoiceField(
        choices=[
            ("Comedy", "Comedy"),
            ("Fantasy", "Fantasy"),
            ("Education", "Education")
        ]
    )
    score = forms.FloatField(min_value = 0.0, max_value=5.0, step_size = 0.5, required=False)
    class Meta:
        model = Movie
        fields = ('title', 'detail', 'genre', 'score',)


class CommentForm(forms.ModelForm):  
    class Meta:
        model = Comment
        fields = ('content',)
