from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the category

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255)  # Name of the medicine
    generic_name = models.CharField(max_length=255, default="N/A")  # Generic name
    description = models.TextField()  # Medicine description
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="medicines",
        default= 'OTC Medicine',  
    )
    Dosage = models.TextField(blank=True, null=True)
    diseases = models.TextField(blank=True, null=True)
    side_effects = models.TextField(blank=True, null=True)  # Optional side effects
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the medicine
    picture = models.ImageField(upload_to='products/',blank=True, null=True)  # Picture of the medicine

    def __str__(self):
        return self.name
