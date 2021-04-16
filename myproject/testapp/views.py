from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView
from .forms import TaskForm, ClientForm
from .models import Task, Client
from django.urls import reverse_lazy

User = get_user_model()


# def index(request):
#     task_list = Task.objects.all()
#     paginator = Paginator(task_list, 10)
#     page_number = request.GET.get('page')
#     page = paginator.get_page(page_number)
#     return render(
#         request,
#         'index.html',
#         {'page': page, 'paginator': paginator, }
#     )


def new_client(request):
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = Client(
                name =  form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                company = form.cleaned_data["company"],
            )
            
            client.save()
            return redirect("index")

        return render(request, 'new_client.html', {'form': form})

    form = ClientForm()
    return render(request, 'new_client.html', {'form': form})

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("index")

        return render(request, 'new.html', {'form': form})

    form = TaskForm()
    return render(request, 'new.html', {'form': form})


class IndexListView(ListView):
    template_name= "task_list.html"
    model = Task


class TackCreate(CreateView):
    template_name = "task_form.html"
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_views")