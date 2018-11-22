from django.urls import path
from post_app import views
app_name = "post_app"

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
]
