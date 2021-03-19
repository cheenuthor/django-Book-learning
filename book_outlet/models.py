from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return self.first_name + " "+self.last_name

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    # if related_name is not set we use Book.objects.author.book_set.all()
    # else we use Book.objects.author.books.all()
    is_best_selling = models.BooleanField(default=False)
    # db_index makes performance better in querying , don't use it for all.
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    # black = True to set the value not required(ADMIN)
    # editable = False to not display the property (ADMIN)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
