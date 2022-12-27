from django.urls import path

from familia_app.views import list_familia, create_familia


urlpatterns = [
    path('create-familia/<str:name>/<str:surname>/<str:age>/<str:have_a_dog>/', create_familia),
    path('', list_familia)
]