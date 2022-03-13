def get_redirect_URL(request):
    search = request.GET.get('search')
    author = request.GET.get('author')
    page = request.GET.get('page')
    if search or author or page:
        url = '/news/?'
        if search:
            url += 'search=' + search + '&'
        if author:
            url += 'author=' + author + '&'
        if page:
            url += 'page=' + page
    else:
        url = '/news/'
    return url
