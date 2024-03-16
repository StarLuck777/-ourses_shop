from django.urls import path, include
from api.models import CourseResource, CategoryResourсe
from tastypie.api import Api


api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResourсe()
api.register(course_resource)
api.register(category_resource)


urlpatterns = [
    path('', include(api.urls), name='index')
]
