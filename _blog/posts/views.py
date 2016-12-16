from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget

from . models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'what', 'when']
        widgets = {
            'when': AdminDateWidget(),
        }


def post_list(request, template_name='posts/post_list.html'):
    posts = Post.objects.all()
    data = {}
    data['post_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='posts/post_form.html'):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form':form})

def post_update(request, pk, template_name='posts/post_form.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form':form})

def post_delete(request, pk, template_name='posts/post_confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, template_name, {'object':post})