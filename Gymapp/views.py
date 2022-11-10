from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from Gymapp.forms import ExerciseFormSet
from Gymapp.models import exercise
# Create your views here.

@login_required
def homepg(request):
    #showall = Exercise.objects.all()
    return render(request, 'home.html', {})

@login_required
def create_workout(request):
    if request.method == 'POST':
        formset = ExerciseFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return render(request, 'home.html', {})
            # do something.
        else:
            return render(request, 'form.html', {'formset': formset})
    else:
        formset = ExerciseFormSet()
    return render(request, 'form.html', {'formset': formset})