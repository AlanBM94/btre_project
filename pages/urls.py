from django.urls import path

from . import views
# First argument is the path where we are going to connect from
# Second argument is the method name we are going to use
# Third argument is the name to easly access this path
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about")
]
