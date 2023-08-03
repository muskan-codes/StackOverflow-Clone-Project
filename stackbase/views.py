from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Comment
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin #it will forbid any other user to update Q. of some other user
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
#Class Based views

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def like_view(request,pk): #views which gonna request particular Q. where like will go that Q. will have pk
    post = get_object_or_404(Question, id=request.POST.get('question_id')) #get Q. id or show 404 error if Q doesnt exist . In django id is automatically generated
    liked = False #first time there will be no likes on the Q
    if post.likes.filter(id = request.user.id).exists(): #if the id exist means user already liked the post
        post.likes.remove(request.user) #remove the liked btn
        liked = False #there is no like
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('stackbase:question_detail', args=[str(pk)]))

class QuestionListView(ListView): 
    model = Question
    context_object_name = 'questions' # context obj name is what u wanna use to refer views in  templates needed in question_list.html in loop {% for question in questions%}
    ordering = ['-date_created']  #it will order questions according to its date created so that latest Q. will come on top
    
    def get_context_data(self, **kwargs): #configure search button
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions']= context['questions'].filter(title__icontains = search_input)
            context['search_input']= search_input 
        return context  

#show Detail of Questions when clicked
class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        something = get_object_or_404(Question, id= self.kwargs['pk'])
        total_likes = something.total_likes()
        liked = False
        if something.likes.filter(id=self.request.user.id).exists():
         liked = True

        context['total_likes']= total_likes
        context['liked'] = liked
        return context


  
#CRUD Functions
# View for Creating a question   
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question 
    fields = ['title', 'content']  

    def form_valid(self, form): #if form filled to create a Q is valid get user info of user and automatically save it to the user id info in db
        form.instance.user = self.request.user
        return super().form_valid(form)

# Updating Q.(Green tick to work)
class QuestionUpdateView( UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self): #This will check if the user who wants to update Q. is the same user that posted the Q.
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False
        
#Delete Question
class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'question'
    success_url = "/" #when Q. is deleted page will be reverted to list page

    def test_func(self): #This will check if the user who wants to delete Q. is the same user that posted the Q.
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False
      
#Create a comment
class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_detail.html'

    def form_valid(self,form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question_detail')

#Add comment from frontend
class AddCommentView(CreateView):
    models = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_answer.html'

    def form_valid(self, form): #saving comment that is posted and redirecting page to question_list
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question_list')
