from django.urls import path

from .views import UserPage, PostCreate, PostDetail, PostDelete



# urlpatterns = [
#     path('user_page', userpage_view, name='user_page'),
# ]

urlpatterns = [
    path('user_page', UserPage.as_view(), name='user_page'),
    path('page_create',PostCreate.as_view(), name='create-post'),
    path('detail/<int:pk>', PostDetail.as_view(), name='user_page'),
    path('delete/<int:pk>', PostDelete.as_view(), name='delete-post'),
]