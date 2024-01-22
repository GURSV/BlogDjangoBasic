from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  # Update the list of displayed fields
    list_filter = ('pub_date',)  # Add a valid filter field
    prepopulated_fields = {'slug': ('title',)}  # Make sure 'slug' is a field in your model

admin.site.register(Post)
