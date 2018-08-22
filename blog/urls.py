from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    # ^는 처음 , $는 끝 처음부터 끝까지 아무것도 없다는 뜻
    url(r'^post/(?P<pk>\d+)/$', views.post_detail , name='post_detail'),
    # 정규표현식 준비한다 ->[]는 \d로 한자리 두자리 세자리 커버 가능 +는 1회 이상 반복될 것이다
    url(r'^post/new/$', views.post_new, name='post_new'),
    # post/new라는 주소로 들어오게 되면 views.post_new로 호출할 것이며 이름은 post_new다
    #url(r'^post/(?P<pk>\d+)/$', views.post_edit , name='post_edit'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]