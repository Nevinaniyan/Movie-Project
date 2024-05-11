from django.contrib import admin
from django.urls import path
from movies import views

app_name="movies"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('details/<int:n>/',views.details,name="details"),
    path('editpage/<int:n>/',views.edit,name="edit"),
    path('delete/<int:n>',views.delete,name="delete"),
    path('add/',views.add,name="add_movies")
]

