from django.shortcuts import render, redirect, get_object_or_404
from .models import PostTag, Post, Comment
from django.db.models import Count
from django.core.paginator import Paginator


def blog_view(request):
    tag = request.GET.get('tag')
    if tag:
        posts = Post.objects.filter(tags=tag, is_published=True).annotate(total=Count('comment')).order_by('-created_at')
    else:
        posts = Post.objects.filter(is_published=True).annotate(total=Count('comment')).order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    recent_posts = Post.objects.filter(is_published=True).order_by('-created_at')

    context = {
        'posts': paginator.page(page),
        'recent_posts': recent_posts,
        'tags': PostTag.objects.all(),
    }

    return render(request, 'blog.html', context)


def blog_single(request, pk):
    if request.method == 'POST':
        Comment.objects.create(post_id=pk, message=request.POST['message'],
                               name=request.POST['name']).save()

        return redirect(f'/blog/{pk}/')

    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by('-created_at')
    recent_posts = Post.objects.filter(is_published=True).order_by('-created_at')

    context = {
        'post': post,
        'tags': PostTag.objects.filter(post=pk),
        'comments': comments,
        'recent_posts': recent_posts,
        'all_tags': PostTag.objects.all(),
    }

    return render(request, 'blog-details.html', context)
