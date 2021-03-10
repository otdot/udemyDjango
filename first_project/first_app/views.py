from django.shortcuts import render
from django.http import HttpResponseRedirect
from first_app.models import User
from first_app.forms import MyNewForm

# Create your views here.
def index(request):
    return render(request,'first_app/index.html')

def users(request):
    user_list = User.objects.order_by('f_name')
    user_dict = {'users': user_list}
    return render(request,'first_app/users.html', context=user_dict)

def form_view(request):
    form = MyNewForm()
    if request.method == "POST":
        form = MyNewForm(request.POST)
        form.save()
        return render(request, 'first_app/index.html', {})
    return render(request, 'first_app/form_page.html', {'form':form})
