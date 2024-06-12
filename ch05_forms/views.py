from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import PostModelForm

# Create your views here.

@login_required(login_url='/admin')
def ex01_post_create(request):
    if request.method == 'POST':
        # Fill form with user input
        form = PostModelForm(request.POST)
        # Save form data to database and return new post (object)
        post = form.save()
        # Redirect user to "success page"
        return redirect(reverse('post_list'))
    else:
        context = {
            'form': PostModelForm()
        }
        return render(request, 'ch05/post_create.html', context)

class PostCreateView(CreateView):
    template_name = 'ch05/post_create.html'
    form_class = PostModelForm

    def get_success_url(self):
        return reverse('post_list')