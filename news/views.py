from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Count, OuterRef, Subquery
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from news.constants import ARTICLES_PER_PAGE
from news.forms import AddNewsArticleForm
from news.models import NewsArticle, Comment, LikeDislike
from praksaPlanetSoft.constants import FIRST_PAGE, HTTP_STATUS_400
from users.models import User


class NewsList(ListView):
    template_name = 'news/news.html'
    model = NewsArticle
    paginate_by = ARTICLES_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', FIRST_PAGE)
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

        context['liked_articles'] = LikeDislike.objects.filter(user_id=self.request.user).all()
        context['object_list'] = news
        context['author_list'] = User.objects.filter(Q(is_editor=True) | Q(is_admin=True), is_active=True)
        return context

    def get_queryset(self, *args, **kwargs):
        has_reacted = LikeDislike.objects.filter(article_id=OuterRef('pk'), user_id=self.request.user.pk)
        queryset = NewsArticle.objects.annotate(
            likes_count=Count('likedislike', filter=Q(likedislike__type=True)),
            dislikes_count=Count('likedislike', filter=Q(likedislike__type=False)),
            liked=Subquery(has_reacted.values('type')))

        search = self.request.GET.get('search')
        author = self.request.GET.get('author')

        if search:
            filtered_query = queryset.filter(Q(headline__icontains=search))
            if len(filtered_query) == 0:
                queryset = queryset.filter(
                    Q(author__first_name__icontains=search) | Q(author__last_name__icontains=search))
            else:
                queryset = filtered_query

        if author and author != 'all':
            queryset = queryset.filter(Q(author__exact=author))

        return queryset


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
        response.status_code = HTTP_STATUS_400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        else:
            raise PermissionDenied("Niste ovlašteni da vršite izmjene vijesti")


class NewsUpdate(UserPassesTestMixin, UpdateView):
    model = NewsArticle
    template_name = 'news/news-edit.html'
    success_url = '/news/'
    form_class = AddNewsArticleForm

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = HTTP_STATUS_400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("Niste ovlašteni da vršite izmjene vijesti")


class NewsPreview(DetailView):
    model = NewsArticle
    template_name = 'news/news-preview.html'
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        context = super(NewsPreview, self).get_context_data(**kwargs)
        has_reacted = LikeDislike.objects.filter(article_id=OuterRef('pk'), user_id=self.request.user.pk)
        context['article'] = NewsArticle.objects.annotate(
            likes_count=Count('likedislike', filter=Q(likedislike__type=True)),
            dislikes_count=Count('likedislike', filter=Q(likedislike__type=False)),
            liked=Subquery(has_reacted.values('type'))).get(id=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(
            article_id=self.kwargs['pk']
        )
        return context


class NewsDelete(UserPassesTestMixin, DeleteView):
    model = NewsArticle
    success_url = '/news/'
    template_name = 'news/news-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("Niste ovlašteni da vršite izmjene vijesti")


@login_required
def likes_dislikes(request, pk):
    liked_disliked_article = None
    if LikeDislike.objects.filter(user_id=request.user.pk, article_id=pk).exists():
        liked_disliked_article = LikeDislike.objects.filter(user_id=request.user.pk, article_id=pk).get()

    if request.headers['flag']:
        if liked_disliked_article is not None and liked_disliked_article.type:
            liked_disliked_article.delete()
        elif liked_disliked_article is not None and not liked_disliked_article.type:
            liked_disliked_article.type = True
            liked_disliked_article.save()
        else:
            LikeDislike.objects.create(user_id=request.user.pk, article_id=pk, type=True)
    else:
        if liked_disliked_article is not None and not liked_disliked_article.type:
            liked_disliked_article.delete()
        elif liked_disliked_article is not None and liked_disliked_article.type:
            liked_disliked_article.type = False
            liked_disliked_article.save()
        else:
            LikeDislike.objects.create(user_id=request.user.pk, article_id=pk, type=False)

    #return HttpResponse(status=HTTP_STATUS_200)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def add_comment(request, pk):
    if request.POST and request.POST.get('content'):
        if request.POST.get('comment'):
            comment = Comment(content=request.POST.get('content'), author=request.user,
                              article=NewsArticle.objects.get(pk=pk), parent_comment=request.POST.get('comment'))
        else:
            comment = Comment(content=request.POST.get('content'), author=request.user,
                              article=NewsArticle.objects.get(pk=pk))
        comment.save()
    #return HttpResponse(status=HTTP_STATUS_200)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AllComments(ListView):
    template_name = 'news/news-comments.html'
    model = Comment
    context_object_name = 'comments'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset().filter(article=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllComments, self).get_context_data(**kwargs)
        has_reacted = LikeDislike.objects.filter(article_id=OuterRef('pk'), user_id=self.request.user.pk)
        context['article'] = NewsArticle.objects.annotate(
            likes_count=Count('likedislike', filter=Q(likedislike__type=True)),
            dislikes_count=Count('likedislike', filter=Q(likedislike__type=False)),
            liked=Subquery(has_reacted.values('type'))).get(id=self.kwargs['pk'])
        return context
