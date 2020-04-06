from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import (
                        DetailView, 
                        ListView, 
                        CreateView, 
                        UpdateView,
                        DeleteView
                        )
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormsUserNeededMixin, UserOwnerMixin

class RetweetView(View):
    def get(self, request,pk,*args,**kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user,tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(FormsUserNeededMixin,LoginRequiredMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    login_url = '/admin/'

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Tweet.objects.all()
    success_url = reverse_lazy("tweet:list")
    template_name = 'tweets/delete_confirm.html'




class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/detail_view.html'
    # def get_object(self):
    #   return Tweet.objects.get(id=1)

class TweetListView(LoginRequiredMixin, ListView):
    def get_queryset(self,*args,**kwargs):
        # template_name = 'tweets/list_view.html'   
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains= query)
                )
        return qs

    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context




# Create your views here.
# def tweet_detail_view(request, id=1):
#   obj  = Tweet.objects.get(id=id)
#   print(obj)
#   context = {
#       'object': obj
#   }
#   return render(request,"tweets/detail_view.html", context)

# def tweet_list_view(request):
#   queryset = Tweet.objects.all()
#   print(queryset)
#   for obj in queryset:
#       print(obj.content)
#   context = {
#       'object_list': queryset
#   }
#   return render(request, "tweets/list_view.html", context)