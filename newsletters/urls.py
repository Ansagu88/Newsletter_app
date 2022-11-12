from django.urls import path
from . import views

app_name = 'newsletters'


urlpatterns = [ 
    path('signup/', views.newsletter_signup, name='signup'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='unsubscribe'),
]