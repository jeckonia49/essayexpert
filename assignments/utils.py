from django.db import models

class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class SubDiscipline(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name="sub_discipline")
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class PaperType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"


class PowerPoint(models.Model):
    count = models.PositiveIntegerField(default=0, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=3.00, editable=False)

    def __str__(self):
        return str(self.count)
    
    @property
    def get_amount(self):
        return f"{(self.count * self.price):2f}"

    def save(self, *args, **kwargs):
        self.price = float(self.get_amount)
        return super(PowerPoint, self).save(*args, **kwargs)


PAPER_TYPE_CHOICES = [(str(paper_type.name), str(paper_type.name)) for paper_type in PaperType.objects.all()]
DISCIPLINE_CHOICES = [(str(discipline.name), str(discipline.name)) for discipline in Discipline.objects.all()]
POWERPOINT_CHOICES = [(int(ppt.count), int(ppt.count)) for ppt in PowerPoint.objects.all()]
