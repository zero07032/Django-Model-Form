from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BlogList, BlogCreate

urlpatterns = [
    path("", BlogList, name="blog-list"),
    path("blog-create", BlogCreate, name="blog-create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
