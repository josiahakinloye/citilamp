from urllib.parse import quote_plus

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView

from .models import Post


class PostDetailView(DetailView):
    template_name = 'post_detail.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        instance = get_object_or_404(Post, slug=slug)
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        instance = context['object']
        context['share_string'] = quote_plus(instance.content)
        return context

def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active().order_by("-timestamp")

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "post_list.html", context)
