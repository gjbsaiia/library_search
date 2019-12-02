from django import forms
from .models import Library, GENRE_CHOICES

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length = 20)

    def getData(self):
        return self.cleaned_data['user_name']

class searchForm(forms.Form):
    lib_choices = []
    libraries = Library.objects.all()
    for each in libraries:
        lib_choices.append((each.name, each.name))
    library_name = forms.ChoiceField(label='Library',choices=lib_choices)
    publisher_name = forms.CharField(label='Publisher', max_length=20, empty_value='')
    book_title = forms.CharField(label='Book Title', max_length=30, empty_value='')
    genre = forms.ChoiceField(label='Genre',choices=GENRE_CHOICES)
    author_name = forms.CharField(label='Author', max_length=20, empty_value='')
    date_published = forms.DateField(label="Date Published")

    def getData(self):
        return self.cleaned_data
