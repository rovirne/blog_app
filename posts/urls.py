from django.urls import path

from . import views

urlpatterns = [
    path('', views.feedView, name="home"),
    path("register/", views.registerView, name="register"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('create-post/', views.createPostView, name="create-post"),
    path('post/<int:pk>/', views.postView,name="post-view"),


]
