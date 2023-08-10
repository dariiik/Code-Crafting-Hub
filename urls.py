#url where my api is available
from django.urls import path
from .views import blog_views
urlpatterns = [
path('posts/', blog_views.PostListCreateAPIView.as_view(), name='api-post-list'),
path('posts/<uuid:pk>/', blog_views.PostDetailsAPIView.as_view(), name='api-post-details'),
]
#application's url
urlpatterns = [
path("admin/", admin.site.urls),
re_path(r'api/(?P<version>[v1|v2]+)/', include('django_blog.apps.blog.rest_api.urls')),
]
