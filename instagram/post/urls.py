from django.urls import path
from .views import HomePageView,CreatePostView,addlike,PostPlus,login_rest


urlpatterns = [
     path('home', HomePageView.as_view(), name='home'),
     path('new_post', CreatePostView.as_view(), name='new_post'),
     path('add_like/<int:pk>', addlike , name='add_like'),
     path('postplus/', PostPlus.as_view() , name='post_plus'),
     path('rest_login/', login_rest , name='login_rest'),

]