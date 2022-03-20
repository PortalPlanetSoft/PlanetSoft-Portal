from django.contrib.auth.decorators import login_required
from django.urls import path

from news.views import NewsList, NewsCreate, NewsUpdate, NewsDelete, likes_dislikes, add_comment, AllComments

urlpatterns = [
    path('', login_required(NewsList.as_view()), name='news'),
    path('create/', login_required(NewsCreate.as_view()), name='news-create'),
    path('<int:pk>/', login_required(NewsUpdate.as_view()), name='news-edit'),
    path('delete/<int:pk>/', login_required(NewsDelete.as_view()), name='news-delete'),
    path('react/<int:pk>/', likes_dislikes, name='like-dislike'),
    path('comment/<int:pk>', add_comment, name='comment-on-news'),
    path('article/<int:pk>', login_required(AllComments.as_view()), name='article-comments'),
]