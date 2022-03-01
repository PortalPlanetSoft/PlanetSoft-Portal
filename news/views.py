from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from news.forms import AddNewsArticleForm
from news.models import NewsArticle
from users.models import User


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
        query_set = super().get_queryset()
        search = self.request.GET.get('search')
        author = self.request.GET.get('author')
        if search:
            filtered_query = query_set.filter(Q(headline__icontains=search))
            if len(filtered_query) == 0:
                query_set = query_set.filter(Q(author__first_name__icontains=search) | Q(author__last_name__icontains=search))
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

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        else:
            raise PermissionDenied("You are not authorized to add new employees")


class NewsUpdate(UserPassesTestMixin, UpdateView):
    model = NewsArticle
    template_name = 'news/news-edit.html'
    success_url = '/news/'
    # form_class = EditNewsArticleForm

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to delete employees")


class NewsDelete(UserPassesTestMixin, DeleteView):
    model = NewsArticle
    success_url = '/news/'
    template_name = 'news/news-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to delete employees")


