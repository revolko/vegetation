from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    last_watered = models.DateTimeField()
    water_frequency_summer = models.IntegerField()
    water_frequency_winter = models.IntegerField()

    class WateringType(models.TextChoices):
        SPRINKLER = 'SP', 'Sprinkler'
        SAUCER = 'SA', 'Saucer'
        PLANTER = 'PL', 'Planter'

    watering_type = models.CharField(
        max_length=2,
        choices=WateringType.choices,
        default=WateringType.SPRINKLER,
    )

    class DroughtTolerance(models.TextChoices):
        LOW = 'L', 'Low'
        MEDIUM = 'M', 'Medium'
        HIGH = 'H', 'High'

    drought_tolerance = models.CharField(
        max_length=1,
        choices=DroughtTolerance.choices,
        default=DroughtTolerance.MEDIUM,
    )

    class LightRequirement(models.TextChoices):
        LOW = 'L', 'Low'
        MEDIUM = 'M', 'Medium'
        HIGH = 'H', 'High'

    light_requirement = models.CharField(
        max_length=1,
        choices=LightRequirement.choices,
        default=LightRequirement.MEDIUM,
    )
