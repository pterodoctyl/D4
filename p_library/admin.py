from django.contrib import admin
from p_library.models import Book, Author, Redaction

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'redaction')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
	pass
