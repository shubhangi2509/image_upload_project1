from django.shortcuts import render,HttpResponse,redirect
from .forms import ImageForm
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin_url')
def title_view(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'uploadimg/title.html'
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='signin_url')
def show_view(request):
    if request.method == 'GET':
        image = Image.objects.all()
        template_name = 'uploadimg/show.html'
        context = {'image':image}
        return render(request,template_name,context)

   # return HttpResponse('<h1>SuccessFul !!!!!!!!</h1>')


def update_view(request,pk):
    obj = Image.objects.get(id=pk)
    form = ImageForm(instance=obj)
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'uploadimg/title.html'
    context = {'form':form}
    return render(request, template_name, context)


def delete_view(request,pk):
    obj = Image.objects.get(id=pk)
    obj.delete()
    return redirect('show_url')



