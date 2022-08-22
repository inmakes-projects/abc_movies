from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='home'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('movie/add/', views.create, name='create_movie'),
    path('movie/edit/<int:movie_id>', views.update, name='update_movie'),
    path('movie/delete/<int:movie_id>', views.delete, name='delete_movie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)