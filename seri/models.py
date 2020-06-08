from django.db import models
from datetime import timedelta
from django.forms import ModelForm 



class GG(models.Model):
    name = models.CharField(max_length=55)
    duration = models.DurationField(default=timedelta(days=3*12*30))

    def __str__(self):
        print(type(self.duration))
        return self.name

class GGForm(ModelForm):
    class Meta:
        model = GG
        fields = "__all__"

class Test(models.Model):
    gg = models.ForeignKey(GG, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name