from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home1.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


# class UserPostListView(ListView):
#     model = Post
#     template_name = 'blog/user_posts.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 5
#
#     def get_query_set(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user)


class PostDetailView(DetailView):
    model = Post



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
