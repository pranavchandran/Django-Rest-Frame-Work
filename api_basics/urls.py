from django.urls import path,include
from api_basics import views
from .views import ArticleList,ArticleDetail,ArticleViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
urlpatterns = router.urls

urlpatterns = [
    # path('article/',views.article_list),
    
    path('article/',ArticleList.as_view()),
    path('article/<int:pk>/',ArticleDetail.as_view()),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),

]

# urlpatterns = format_suffix_patterns(urlpatterns)