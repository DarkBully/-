from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView
from django.urls import reverse

from .serializers import CommentSerializer
from .forms import CommentsForm
from .models import Comment

from rest_framework import viewsets
from rest_framework import mixins


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    
    def get_success_url(self):
        return reverse('detail-post',kwargs={'pk':self.object.post.id})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentsForm
    
    def get_success_url(self):
        return reverse('detail-post',kwargs={'pk':self.object.post.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class CommentViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
