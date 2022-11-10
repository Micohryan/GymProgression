from django import forms
from Gymapp.models import exercise
from django.forms import modelformset_factory

ExerciseFormSet = modelformset_factory(exercise, fields=('exercise', 'reps', 'weight', 'completed'))