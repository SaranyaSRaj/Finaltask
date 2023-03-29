from django.urls import path

from.import views

app_name='taskapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('registration/',views.registration,name="registration"),
    path('getdata/', views.getdata, name="getdata"),
    path('Category', views.branch, name='products_by_category'),
    path('logout',views.logout,name="logout"),

]