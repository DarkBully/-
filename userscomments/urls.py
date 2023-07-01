from django.urls import path
from .views import CommentDeleteView, CommentCreateView



urlpatterns = [
    path('createcomment', CommentCreateView.as_view(), name='create-comment'),
    path('deletecomment<int:pk>', CommentDeleteView.as_view(), name='delete-comment')
]