from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from woodpecker import settings
from woodpecker.views import IndexView, TestView

urlpatterns = [
    # Examples:
    # url(r'^$', 'woodpecker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', IndexView.as_view(), name='home'),

    url(r'^register/', include('register.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^logout/', logout, {"next_page": "/", "redirect_field_name": "/"},
        name="logout"),
    url(r'^user/', include('user.urls')),
    url(r'^task/', include('task.urls')),
    url(r'^analysis/', include('analysis.urls')),

    url(r'^dict/', include('dict.urls')),
    url(r'^test/', TestView.as_view()),
    # url(r'^mine/', include('apps.mine.urls')),
]

if not settings.DEBUG:
    urlpatterns += (
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
