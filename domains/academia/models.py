from django.db import models


# institution model
class Institution(models.Model):

    # primary information
    name = models.CharField(max_length=250, unique=True, verbose_name="Institution Name")
    country = models.CharField(max_length=100, verbose_name="Country")
    city = models.CharField(max_length=100, verbose_name="City")

    # secondary information
    address = models.TextField(blank=True, null=True, verbose_name="Institution Address")
    website = models.URLField(blank=True, null=True, verbose_name="Institution Website")
    phone_number = models.CharField(blank=True, null=True, verbose_name="Institution Phone Number")
    email = models.EmailField(blank=True, null=True, verbose_name="Institution Email Address")
    established_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Established Year")

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["country", "city", "established_year", "name"]

    def __str__(self):
        return f"{self.name}, {self.city}, {self.country}"


# subject model
class Subject(models.Model):

    # primary information
    name = models.CharField(max_length=255, verbose_name="Subject Name")
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name="Subject Code")

    # secondary information
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Parent Subject")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, code: {self.code}"
