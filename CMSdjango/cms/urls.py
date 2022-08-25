from django.urls import path
from . import views

# app_name = "cms"

urlpatterns = [
    # Leave as empty string for base url
    # path('',views.Catalog, name="Catalog"),
    path('CC',views.CC, name="CC"),
    path('CO',views.CO, name="CO"),
    # path('Update_Profile',views.user_profile, name="Update_Profile"),
    # path('Preview',views.Preview, name="Preview"),
    # path('',views.secsignin, name="secsignin"),
    # path('Register',views.register, name="register"),
    # path('<int:User_id>/',views.display, name="display"),
    path('Catalog',views.Catalog, name="Catalog"),
    path('Signup',views.sign_up, name="register"),
    path('',views.user_login, name="login"),
    path('profile',views.user_profile, name="profile"),
    path('changepass',views.user_change_pass, name="changepass"),
    path('Units',views.Units, name="Units"),
    path('Update_Course/<int:id>',views.Update_Course, name="Update_Course"),
    path('Delete_Course/<int:id>',views.Delete_Course, name="Delete_Course"),
    path('logout', views.user_logout, name="logout")

]