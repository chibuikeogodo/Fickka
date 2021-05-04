from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, Thread, About
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import PostForm, CommentForm, ThreadForm, UpdateForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView, TemplateView
from django.contrib.auth.forms import UserChangeForm
from django.views import View
from django.contrib.auth.forms import User
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin, messages

from members.forms import PasswordChangeForms


class AboutPage(ListView):
    model = About
    template_name = 'about.html'

def ContactUs(request):
    return render(request, 'contact.html')


def likeView(request, pk, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return redirect(post.get_absolute_url())



class home(ListView):
    template_name = 'home.html'
    cats = Category.objects.all()
    user = User.objects.all()
    ordering = ['-pk']
    paginate_by = 15
    context_object_name = 'tasks'

    def get_queryset(self):
        return Post.objects.filter(To_homepage=True).order_by('-post_number')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class Last_Post(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'last'
    paginate_by = 5



class Search(ListView):
    model = Post
    cats = Category.objects.all()
    user = User.objects.all()
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(post_title__icontains=query)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Search, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class Control(ListView):
    template_name = 'all.html'
    cats = Category.objects.all()
    context_object_name = 'tasks'
    ordering = ['date']

    def get_queryset(self):
        return Post.objects.filter(To_homepage=False).order_by('-date_posted')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Control, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        search_input = self.request.GET.get('search-text') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context


class PostCategory(ListView):
    model = Post
    ordering = ['date_posted']
    paginate_by = 15
    template_name = 'category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CreateCategory(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'create_cat.html'
    form_class = CategoryForm
    success_url = reverse_lazy('create_cate')
    success_message = '%(name)s was added to Category list successfully'



class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    # fields = '__all__'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def article(request, id, slug):
    post = get_object_or_404(Post, id=id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    post.views= post.views + 1
    post.save()
    comment = Comment.objects.filter(post=post).order_by('id')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('comment')
            comments = Comment.objects.create(post=post, name=request.user, comment=content)
            comments.save()
            messages.success(request, 'Your comment has being posted successfully')
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'liked': liked,
        'total_likes': post.total_likes(),
        'comment': comment,
        'comment_form': comment_form,
    }
    return render(request, 'article.html', context)



def Thrend(request, id):
    post = get_object_or_404(Post, id=id)
    threands = Thread.objects.filter(post=post)

    if request.method == 'POST':
        thread_form = ThreadForm(request.POST or None, request.FILES or None)
        if thread_form.is_valid():
            threndy = request.POST.get('threads')
            image1 = request.FILES.get('image_1')
            image2 = request.FILES.get('image_2')
            image3 = request.FILES.get('image_3')
            thrend = Thread.objects.create(post=post, name=request.user, threads=threndy, image_1=image1, image_2=image2, image_3=image3)
            messages.success(request, 'Your post has being updated successfully')
            thrend.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        thread_form = ThreadForm()

    context = {
        'threads': threands,
        'thread_form': thread_form,
    }

    return render(request, 'add_thrend.html', context)


class Update_post(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = UpdateForm
    success_url = reverse_lazy('home')


class CommentReplyView(LoginRequiredMixin, View):
    ordering = ('-date')

    def post(self, request, post_pk, pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            messages.success(request, 'Your reply has being posted successfully')
            new_comment.save()

        return redirect(post.get_absolute_url())


class UserPostList(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs['pk']).order_by('-date_posted')


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForms
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change')