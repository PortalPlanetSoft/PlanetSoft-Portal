from django.contrib.auth.decorators import login_required
from django.urls import path

from news.views import NewsList, NewsCreate, NewsUpdate, NewsDelete, likes_dislikes, add_comment, AllComments, \
    NewsPreview, remove_news_photo, likes_dislikes_comment

urlpatterns = [
    path('', login_required(NewsList.as_view()), name='news'),
    path('create/', login_required(NewsCreate.as_view()), name='news-create'),
    path('<int:pk>/', login_required(NewsUpdate.as_view()), name='news-edit'),
    path('delete/<int:pk>/', login_required(NewsDelete.as_view()), name='news-delete'),
    path('react/<int:pk>/', likes_dislikes, name='like-dislike'),
    path('comment/<int:pk>', add_comment, name='comment-on-news'),
    path('article/<int:pk>', login_required(AllComments.as_view()), name='news-comments'),
    path('article/preview/<int:pk>', login_required(NewsPreview.as_view()), name='news-preview'),
    path('remove-photo/<int:pk>', remove_news_photo, name='remove-photo'),
    path('likes_dislikes_comment/<int:pk>', likes_dislikes_comment, name='likes_dislike_comment')
]
