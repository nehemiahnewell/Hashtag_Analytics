from django.conf.urls import include, url
from django.contrib import admin
import takedata.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Hashtag_analytics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', takedata.views.start_home_page, name='home'),
    url(r'^records/', takedata.views.start_arhive_page, name='records'),
    url(r'^(?P<hashSearch_id>\d+)/$',takedata.views.search, name="search")

]
