from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string




def home(request, *args, **kwargs):
    article_obj = Article.objects.get(id=2)
    list_obj = Article.objects.all()

    context = {
        "obj": article_obj,
        "list_obj": list_obj
    }


    html = render_to_string(template_name="home-view.html", context=context)
    return HttpResponse(html)
