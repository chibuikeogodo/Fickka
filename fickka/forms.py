from django import forms
from . models import Post, Comment, Thread, Category
from emoji_picker.widgets import EmojiPickerTextareaAdmin, EmojiPickerTextarea


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image_1', 'image_2', 'image_3')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '7'}),
            'category': forms.Select(attrs={'class': 'custom-select'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('threads', 'image_1', 'image_2', 'image_3')

        widgets = {
            'threads': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title','post_number','title', 'To_homepage', 'content', 'category')

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control','placeholder':' This will show on the homepage'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '12',  'readonly': 'readonly'}),
            'category': forms.Select(attrs={'class': 'form-control',  'readonly': 'readonly'}),

        }



