from django.db import models

# Create your models here.

#class Exercise(models.Model):
#    exercise = models.CharField(max_length = 1000, blank = False)
#    class Meta:
#        db_table = 'Exercise Names'

class exercise(models.Model):
    exercise = models.CharField(max_length = 1000, blank = False)
    reps = models.PositiveIntegerField(default = 0)
    weight = models.PositiveIntegerField(default = 0)
    completed = models.BooleanField(default = False)
    class Meta:
        db_table = 'Sets and Reps'

#class exercise_sets:
    #exercise_name = models.ForeignKey(Exercise, on_delete = models.CASCADE)
    #exercise = models.CharField(max_length = 1000, blank = False)
#    sets = models.ForeignKey(sets_reps)
 #   reps = models.ForeignKey(sets_reps)
 #   class Meta:
  #      db_table = 'Exercise Template'
