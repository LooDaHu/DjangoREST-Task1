from django.urls import path
from . import views

urlpatterns = (
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('hello', views.hello_world),
    path('time_gap/<int:pk1>&<int:pk2>', views.get_time_gap, name='Time Gap')
    path('time_query/<str:time1>&<str:time2>', views.get_posts_with_time)
)


