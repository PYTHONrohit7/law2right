from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Post
from .forms import ContactForm


def _common_context():
    return {'categories': Category.objects.all()}


def home(request):
    categories = Category.objects.all()
    latest_news = Post.objects.none()
    try:
        news_cat = categories.get(slug='daily-legal-news-updates')
        latest_news = Post.objects.filter(category=news_cat).order_by('-created_at')[:3]
    except Category.DoesNotExist:
        pass

    exam_highlight = None
    try:
        exam_cat = categories.get(slug='law-exams-preparation')
        exam_highlight = Post.objects.filter(category=exam_cat).order_by('-created_at')[:1]
    except Category.DoesNotExist:
        exam_highlight = Post.objects.none()

    featured_posts = Post.objects.filter(is_featured=True).order_by('-created_at')[:5]

    ctx = {
        'latest_news': latest_news,
        'exam_highlight': exam_highlight,
        'featured_posts': featured_posts,
        **_common_context(),
    }
    return render(request, 'core/home.html', ctx)


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.order_by('-created_at')
    ctx = {'category': category, 'posts': posts, **_common_context()}
    return render(request, 'core/category_list.html', ctx)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    ctx = {'post': post, **_common_context()}
    return render(request, 'core/post_detail.html', ctx)


def search(request):
    q = request.GET.get('q', '').strip()
    posts = Post.objects.none()
    if q:
        posts = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).order_by('-created_at')
    ctx = {'query': q, 'posts': posts, **_common_context()}
    return render(request, 'core/search_results.html', ctx)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:contact_thanks')
    else:
        form = ContactForm()
    ctx = {'form': form, **_common_context()}
    return render(request, 'core/contact.html', ctx)


def contact_thanks(request):
    return render(request, 'core/contact_thanks.html', _common_context())


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html', _common_context())


def about(request):
    return render(request, 'core/about.html', _common_context())
