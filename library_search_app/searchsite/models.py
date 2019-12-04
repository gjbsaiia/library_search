from django.db import models
from datetime import timedelta, date

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

genres = [
    'non-fiction',
    'children',
    'drama',
    'fantasy',
    'graphic novel',
    'horror',
    'mystery',
    'poetry',
    'romance',
    'satire',
    'biography',
    'auto-biography',
    'thriller',
    'young adult',
    'other',
]

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

def validate_genre(genre):
    genre = genre.lower()
    if genre not in genres:
        raise ValidationError('ERROR: unsupported genre.')

def validate_count(count):
    if count <= 0:
        raise ValidationError('ERROR: Non-real book count.')

class Library(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    address = models.CharField(unique=True, max_length=30)
    dateFounded = models.DateField(null=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.address)

class Publisher(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "%s"%(self.name)

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=18,
                             choices=GENRE_CHOICES,
                             validators=[validate_genre],
                             default="other")
    publisher_ID = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    datePublished = models.DateField(null=True)

    def getTitle(self):
        return "%s" % (self.title)

    def __str__(self):
        if(self.description):
            des = self.description
        else:
            des = "No Description Available."
        if(self.datePublished):
            return "%s, %s, %s, %s\n%s"%(self.title, self.genre, str(self.publisher_ID), str(self.datePublished), self.description)
        else:
            return "TITLE: %s,GENRE: %s,PUBLISHER: %s,DATE PUBLISHED: %s\nDESCRIPTION:\n%s"%(self.title, self.genre, str(self.publisher_ID), "PUBLISH DATE NOT LISTED", self.description)

class Author(models.Model):
    name = models.CharField(max_length=20)
    DOB = models.DateField(null=True)

    def __str__(self):
        return "%s"%(self.name)

class Library_Books(models.Model):
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    book_ID = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.FloatField(validators=[validate_count])

    def __str__(self):
        return "%s, has %d copies of %s" % (str(self.library_name), self.count, str(self.book_ID.getTitle()))

    class Meta:
        unique_together = (("library_name", "book_ID"))

class Written_By(models.Model):
    book_ID = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_ID = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "%s"%(str(self.author_ID))

    class Meta:
        unique_together = (("book_ID", "author_ID"))


class User_Manager(models.Manager):
    def newUser(self, name):
        user = self.create(name=name)
        return user

class User(models.Model):
    name = models.CharField(max_length=20)

    objects = User_Manager()

    def __str__(self):
        return "%s"%(self.name)


class CheckOut_Manager(models.Manager):
    def new_checkout(self, user, book, library):
        query = Library_Books.objects.filter(library_name=library, book_ID=book).exclude(count__lt=1)
        if(query):
            lb = Library_Books.objects.get(pk = query[0])
            lb -= 1
            lb.save()
            duedate = date.today() + timedelta(weeks=1)
            checkout = self.create(user_ID=user, book_ID=book, library_name=library, due=duedate)
            return checkout


class Checks_Out(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    book_ID = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    due = models.DateField()
    objects = CheckOut_Manager()

    def __str__(self):
        return "Receipt for %s: \nCHECKED OUT FROM:\n   %s\n\n%s IS DUE ON %s" % (str(self.user_ID), str(self.library_name), self.book_ID.getTitle(), str(self.due))

    class Meta:
        unique_together = (("user_ID", "book_ID", "library_name"))

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)

    def getLibraryName(self):
        return self.library_name.name

    def __str__(self):
        return "%s at %s"%(self.name, str(self.library_name))

class Librarian_Genre(models.Model):
    librarian_ID = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    genre = models.CharField(max_length=18,
                            choices=GENRE_CHOICES,
                            validators=[validate_genre],
                            default="other")

    def __str__(self):
        return "%s:     %s"%(str(self.librarian_ID), self.genre)

    class Meta:
        unique_together = (("librarian_ID", "genre"))
