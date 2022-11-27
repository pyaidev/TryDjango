from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Article
from .forms import ArticleCreateForm


def article_list_view(request):
    articles = Article.objects.all()
    context = {
        'object_list': articles
    }
    return render(request, 'articles/list.html', context)


@login_required
def _article_detail_view(request, pk=None):
    article_obj = None
    if pk is not None:
        article_obj = Article.objects.get(id=pk)

    context = {
        'object': article_obj
    }
    return render(request, 'articles/detail.html', context)


@login_required
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except Exception as e:
            raise e.args

    context = {
        'object': article_obj
    }
    return render(request, 'articles/detail.html', context)


def article_search_view(request):
    # print(request.GET)
    query_dict = request.GET
    query = query_dict.get('q')
    articles = None
    if query:

        articles = Article.objects.search(query)
    context = {
        'object_list': articles
    }
    return render(request, 'articles/search.html', context)


def _article_create_view(request):
    query_dict = request.POST
    # print(query_dict)
    title = query_dict.get('title')
    content = query_dict.get('content')
    context = {}
    if title:
        object = Article.objects.create(title=title, content=content)
        context['object'] = object

    return render(request, 'articles/create.html', context)


def __article_create_view(request):
    form = ArticleCreateForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        object = Article.objects.create(title=title, content=content)
        context['object'] = object

    return render(request, 'articles/create.html', context)

@login_required
def article_create_view(request):
    form = ArticleCreateForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        object = form.save()
        context['object'] = object

    return render(request, 'articles/create.html', context)


@login_required()
def article_update_view(request, pk=None):
    article_obj = None
    if pk is not None:
        article_obj = Article.objects.get(id=pk)
    form = ArticleCreateForm(instance=article_obj)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    if request.method == 'POST':
        # article_obj.title = title
        # article_obj.content = content
        # article_obj.save()
        form = ArticleCreateForm(request.POST, instance=article_obj)
        if form.is_valid():
            form.save()
            return redirect('articles:article_detail', article_obj.id)
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


@login_required()
def article_delete_view(request, pk=None):
    article_obj = None
    if pk is not None:
        article_obj = Article.objects.get(id=pk)
    if request.method == 'POST':
        article_obj.delete()
        return redirect('/')
    context = {
        'object': article_obj
    }
    return render(request, 'articles/delete.html', context)

