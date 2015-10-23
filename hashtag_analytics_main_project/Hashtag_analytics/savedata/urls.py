from django.conf.urls import include, url
from django.contrib import admin
import savedata.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Hashtag_analytics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', savedata.views.perform_search, name='records'),

]
