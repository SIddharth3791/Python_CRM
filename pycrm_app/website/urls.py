
from . import views
from django.urls import  path

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('user/<int:pk>',views.user_details, name='user_details'),
    path('delete_user/<int:pk>',views.delete_user, name='delete_user'),
    path('add_user/',views.add_user, name='add_user'),
    path('update_user/<int:pk>', views.update_user, name='update_user')
]
