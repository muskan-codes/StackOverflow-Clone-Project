from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('',views.home , name="home"),
    path('about/', views.base, name="base"),

    #CRUD Function
    path('questions/', views.QuestionListView.as_view(), name="question_list"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name = "question_detail"),
    path('questions/new/' , views.QuestionCreateView.as_view(), name="question_create"),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name="question_update"),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name= "question_confirm_delete"),
    path('questions/<int:pk>/comment/', views.AddCommentView.as_view(), name= "question_comment"),
    path('like/<int:pk>', views.like_view, name="like_post")
]
