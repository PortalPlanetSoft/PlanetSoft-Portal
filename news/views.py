from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect

from news.forms import AddNewsArticleForm
from news.models import NewsArticle, Comment
from users.models import User
from news.util import get_redirect_URL


class NewsList(ListView):
    template_name = 'news/news.html'
    model = NewsArticle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        news = self.object_list.order_by('headline')
        paginator = self.paginator_class(news, self.paginate_by)
        news = paginator.page(page)

        # parametar autora za GET request
        if self.request.GET.get('author'):
            if self.request.GET.get('author') == 'all':
                context['selected'] = 'all'
            else:
                context['selected'] = int(self.request.GET.get('author'))
        # parametar pretrage za GET request
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')
        # parametar autora za GET request
        if self.request.GET.get('author'):
            context['author'] = self.request.GET.get('author')

        context['object_list'] = news
        context['author_list'] = User.objects.filter((Q(is_editor=True) | Q(is_admin=True) | Q(is_superuser=True)),
                                                     is_active=True)
        return context

    def get_queryset(self, *args, **kwargs):
        # query_set = super().get_queryset()
        query_set = NewsArticle.objects.annotate(Count('likes'), Count('dislikes'))
        search = self.request.GET.get('search')
        author = self.request.GET.get('author')
        if search:
            filtered_query = query_set.filter(Q(headline__icontains=search))
            if len(filtered_query) == 0:
                query_set = query_set.filter(
                    Q(author__first_name__icontains=search) | Q(author__last_name__icontains=search))
            else:
                query_set = filtered_query

        if author and author != 'all':
            query_set = query_set.filter(Q(author__exact=author))

        return query_set


class NewsCreate(UserPassesTestMixin, CreateView):
    model = NewsArticle
    template_name = 'news/news-create.html'
    success_url = '/news/'
    form_class = AddNewsArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        else:
            raise PermissionDenied("You are not authorized to add new news articles")


class NewsUpdate(UserPassesTestMixin, UpdateView):
    model = NewsArticle
    template_name = 'news/news-edit.html'
    success_url = '/news/'
    form_class = AddNewsArticleForm

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to edit news articles")


class NewsDelete(UserPassesTestMixin, DeleteView):
    model = NewsArticle
    success_url = '/news/'
    template_name = 'news/news-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to delete news articles")


@login_required
def likes_dislikes(request, pk):
    article = get_object_or_404(NewsArticle, id=pk)
    if request.POST.get('article_like_id'):
        if article.dislikes.filter(id=request.user.pk):
            article.dislikes.remove(request.user)
        article.likes.add(request.user)
    else:
        if article.likes.filter(id=request.user.pk):
            article.likes.remove(request.user)
        article.dislikes.add(request.user)

    url = get_redirect_URL(request)
    return HttpResponseRedirect(url)


@login_required
def add_comment(request, pk):
    if request.POST and request.POST.get('content'):
        comment = Comment(content=request.POST.get('content'), author=request.user,
                          article=NewsArticle.objects.get(pk=pk))
        comment.save()
    url = get_redirect_URL(request)
    return HttpResponseRedirect(url)


class AllComments(ListView):
    template_name = 'news/article-comments.html'
    model = Comment
    context_object_name = 'comments'

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset().filter(article=self.kwargs['pk'])
        return query_set

    def get_context_data(self, **kwargs):
        context = super(AllComments, self).get_context_data(**kwargs)
        context['article'] = NewsArticle.objects.annotate(Count('likes'), Count('dislikes')).get(id=self.kwargs['pk'])
        return context
