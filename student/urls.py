from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('grades', views.GradeViewSet, basename='grades')
router.register('sections', views.SectionViewSet, basename='sections')
router.register('users', views.UserViewSet, basename='users')

grade_route = routers.NestedDefaultRouter(router, 'grades', lookup='grade')
grade_route.register('sections', views.NestedSectionViewSet, basename='grade-sections')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(grade_route.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
