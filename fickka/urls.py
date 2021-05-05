from django.urls import path
from .views import home, PostCategory, CreatePost, \
    article,likeView, Thrend, Update_post, Control, \
    CommentReplyView, AboutPage, ContactUs, Search, \
    CreateCategory, UserPostList, PasswordChangeView, \
    Control, DeletePost
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home.as_view(), name='home'),
    path('control', Control.as_view(), name='control'),
    path('search_results/', Search.as_view(), name='search_result'),
    path('category/<int:pk>/', PostCategory.as_view(), name='category_list'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('create_category', CreateCategory.as_view(), name='create_category'),
    path('new_fick', CreatePost.as_view(), name='create_post'),
    path('article/<int:id>/<slug:slug>', article, name='article'),
    path('post/<int:post_pk>/comment/<int:pk>/replay', CommentReplyView.as_view(), name='comment_replay'),
    path('like/<int:pk>/<slug:slug>/', likeView, name='like_post'),
    path('add/<int:id>/thread', Thrend, name='add_thrend'),
    path('update/fick/<int:pk>', Update_post.as_view(), name='update_post'),
    path('About', AboutPage.as_view(), name='about_us'),
    path('contact_us', ContactUs, name='contact_us'),
    path('user_post/<int:pk>/', UserPostList.as_view(), name='user_post_list'),
    path('password/', PasswordChangeView.as_view(), name='change_password'),


]
