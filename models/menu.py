response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Unveröffentlichte Bücher'),URL('default','return_unpublished_books')==URL(),URL('default','return_unpublished_books'),[]),
(T('Veröffentlichte Bücher'),URL('default','return_published_books')==URL(),URL('default','return_published_books'),[]),
]
