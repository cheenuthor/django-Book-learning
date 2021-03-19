from book_outlet.models import Address, Author, Book
from django.contrib import admin

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author", "rating")


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author,
                     #  AuthorAdmin
                     )
admin.site.register(Address)