from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView

from .forms import UserPageForm
from .models import Post
from .serializers import PostSerializer

from userscomments.forms import CommentsForm

from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework import viewsets, permissions



class UserPage(ListView):
    model = Post
    template_name = 'user/user_page.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_page'] = True
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'user/user_page.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentsForm(
            initial={'post':context['post'].id}
        )
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = UserPageForm
    template_name = 'user/page_create.html'
    
    def get_success_url(self):
        return reverse('create-post')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    def get_success_url(self):
        return reverse('user_page')


# class UserViewSet(mixins.ListModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.UpdateModelMixin,
#                     viewsets.GenericViewSet):
#     queryset = Post.objects.all()
#     serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer