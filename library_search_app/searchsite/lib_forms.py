from django import forms

GENRE_CHOICES = (
    ('Non-Fiction',     'non-fiction'),
    ('Children',         'children'),
    ('Drama',            'drama'),
    ('Fantasy',          'fantasy'),
    ('Graphic Novel',    'graphic novel'),
    ('Horror',           'horror'),
    ('Mystery',          'mystery'),
    ('Poetry',           'poetry'),
    ('Romance',          'romance'),
    ('Satire',           'satire'),
    ('Biography',        'biography'),
    ('Auto-Biography',   'auto-biography'),
    ('Thriller',         'thriller'),
    ('Young Adult',      'young adult'),
    ('other',            'other'),
)

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
