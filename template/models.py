from django.db import models

# Create your models here.


class BackgroundScore(models.Model):
    score_url = models.FileField(upload_to='media', null=True)
    start_time = models.FloatField()
    end_time = models.FloatField()


class Components(models.Model):
    slot_id = models.IntegerField()
    component_url = models.FileField(upload_to='media', null=True)
    component_start_time = models.FloatField()


class TextElement(models.Model):
    text = models.CharField(max_length=100)
    font = models.CharField(max_length=30)
    font_size = models.CharField(max_length=10)
    position_x = models.CharField(max_length=10)
    position_y = models.CharField(max_length=10)
    start_time = models.FloatField()
    end_time = models.FloatField()

    def __str__(self):
        return self.font


class Logos(models.Model):
    logo_url = models.FileField(upload_to='media', null=True)
    start_time = models.FloatField()
    end_time = models.FloatField()
    transition_in = models.CharField(max_length=20)
    transition_out = models.CharField(max_length=20)


class Overlays(models.Model):
    text_element = models.ManyToManyField(TextElement)
    logos = models.ManyToManyField(Logos)


class Template(models.Model):
    business = models.CharField(max_length=50)
    types = models.CharField(max_length=30)
    watermark = models.CharField(max_length=30)
    duration = models.DurationField()
    template_url = models.FileField(upload_to='media', null=True)
    background_score = models.ForeignKey(
        BackgroundScore, on_delete=models.CASCADE)
    components = models.ManyToManyField(Components)
    overlays = models.ForeignKey(Overlays, on_delete=models.CASCADE)
