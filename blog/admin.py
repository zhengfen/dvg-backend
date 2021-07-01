from django.contrib import admin

# Register your models here.
from blog.models import Profile, Post, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): 
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin): 
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    
    # In the list of all posts, only show the following information about each post
    list_display = (
        "id", 
        "title", 
        "subtitle",
        "slug", 
        "publish_date", 
        "published",
    )
    # Allow filtering the post list by posts that are published or unpublished.
    # Allow filtering posts by publish date.
    list_filter = (
        "published", 
        "publish_date",
    )
    # Allow editing all the displayed fields, with the exception of the ID.
    list_editable = (
        "title",
        "subtitle", 
        "slug", 
        "publish_date", 
        "published"
    )
    # Allow searching for posts using the title, subtitle, slug, and body.
    search_fields = (
        "title", 
        "subtitle", 
        "slug", 
        "body"
    )
    # Prepopulate the slug field using the title and subtitle fields.
    prepopulated_fields = {
        "slug": (
            "title", 
            "subtitle"
        )
    }
    # Use the publish date of all posts to create a browsable date hierarchy.
    date_hierarchy = "publish_date"
    # Show a button at the top of the list to save changes.
    save_on_top = True

    

