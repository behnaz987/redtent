from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('users/', views.users_list),
    #path('snippets/<int:pk>', views.snippet_detail),
]