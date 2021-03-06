from django.conf.urls import include, url
from django.contrib import admin
from takedata.views import start_home_page


urlpatterns = [
    # Examples:
    # url(r'^$', 'Hashtag_analytics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hashtag_search/', include('takedata.urls', namespace='hash')),
    url(r'^search_string/', include('savedata.urls', namespace='search_string')),
    url(r'^$',start_home_page, name='table_of_contents')
]
