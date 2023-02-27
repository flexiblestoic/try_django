from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.

def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {'object': article_obj}
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    

    context['form'] = form
    #print(form)

    if form.is_valid():
        object = form.save()
        form = ArticleForm()
        context = {"object": object, 'form': form}

    return render(request, "articles/create.html", context=context)

# @login_required
# def article_create_view(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
    
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         #print(form)

#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             print(form)
#             content = form.cleaned_data.get('content')
#             object = Article.objects.create(title = title, content = content)
#             context = {"object": object}

#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):

    article_obj = None
    
    if id is not None:
        article_obj = Article.objects.get(id=id)
        context = {
            "object": article_obj,
        }
    return render(request, "articles/details.html", context=context)