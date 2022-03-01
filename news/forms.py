from news.models import NewsArticle
from django import forms

ERROR_MESSAGES = {
}


class AddNewsArticleForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = NewsArticle
        fields = {'headline', 'content'}

        widgets = {
            'headline': forms.TextInput(attrs={'placeholder': 'Naslov'}),
            'content': forms.Textarea(attrs={'placeholder': 'Sadržaj'}),
        }


    # todo ovo jos nije implementirano ali bice
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(AddNewsArticleForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        news_article = super(AddNewsArticleForm, self).save(commit=False)
        news_article.set_author(self.request.user.id)
        if commit:
            news_article.save()
        return news_article

