from django.urls import path,re_path
from post_app import views
app_name = "post_app"

urlpatterns = [
    path('',views.About.as_view(),name="about"),
    path('list/',views.PostListView.as_view(),name="list"),
    path('drafts/',views.DraftListView.as_view(),name="drafts"),
    path('post/new/',views.CreatePostView.as_view(),name="new_post"),
    re_path(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name="post_detail"),
    re_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name="post_edit"),
    re_path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name="post_publish"),
    re_path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name="post_delete"),
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name="comment_new"),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name="comment_approve"),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name="comment_remove"),    
]
