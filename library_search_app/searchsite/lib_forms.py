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
    library_name = forms.CharField(label='Library',max_length=20, blank=True, null=True)
    publisher_name = forms.CharField(label='Publisher', max_length=20, blank=True, null=True)
    book_title = forms.CharField(label='Book Title', max_length=30, blank=True, null=True)
    genre = forms.ChoiceField(label='Genre',choices=GENRE_CHOICES, initial='')
    author_name = forms.CharField(label='Author', max_length=20, blank=True, null=True)
    date_published = forms.DateField(label="Date Published", blank=True, null=True)

    def getData(self):
        return self.cleaned_data or None
