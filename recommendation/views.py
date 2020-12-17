from django.shortcuts import render, redirect
from .models import UserForRec
from .forms import UserForRecForm
from django.views.generic import DetailView, UpdateView, DeleteView


def recom_home(request):
    users = UserForRec.objects.all()
    return render(request, 'recommendation/recom_home.html', {'users': users})


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserForRecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recom_home')
        else:
            error = 'Некорретно введены данные'

    form = UserForRecForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'recommendation/create.html', data)


class RecommendationDetail(DetailView):
    model = UserForRec
    template_name = 'recommendation/details_view.html'
    context_object_name = 'recommendation'


class RecommendationUpdate(UpdateView):
    model = UserForRec
    template_name = 'recommendation/create.html'

    form_class = UserForRecForm

class RecommendationDelete(DeleteView):
    model = UserForRec
    template_name = 'recommendation/delete.html'
    success_url = '/recommendation/'
