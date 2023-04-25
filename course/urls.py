from django.urls import path

from . import views


urlpatterns = [
    path('viewset/course/', views.CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('viewset/course/<int:pk>/', views.CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),

    path('student/', views.StudentListCreateAPIView.as_view()),
    path('student/<int:student_id>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('mentor/', views.MentorListCreateAPIView.as_view()),
    path('mentor/<int:mentor_id>/', views.MentorRetrieveUpdateDestroyAPIView.as_view()),
]