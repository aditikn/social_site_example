from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/update/(?P<pk>\d+)$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/delete/(?P<pk>\d+)$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft'),
    url(r'^post/comment/(?P<pk>\d+)/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/approve/(?P<pk>\d+)$', views.comment_approve, name='comment_approve'),
    url(r'^comment/remove/(?P<pk>\d+)$', views.comment_remove, name='comment_remove'),
    url(r'^post/publish/(?P<pk>\d+)$', views.post_publish, name='post_publish'),
]
