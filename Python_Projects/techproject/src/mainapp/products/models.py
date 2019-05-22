from django.db import models


TYPE_CHOICES = {
    ('appetizers','appetizers'),
    ('entrees','entrees'),
    ('treats','treats'),
    ('drinks','drinks'),
}


class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)

    objects = models.Manager()
    # NOTE: We do the line above to then be able to name our product object. On the
    # https://docs.djangoproject.com/en/2.2/topics/db/managers/#manager-names
    # documentation, it says you must define a class attribute of type models.Manager() on
    # the model we're on.


    def __str__(self):
        return self.name
    # Python's integrated dunder method __str__() can convert an object name to a string value that
    # would make more sense to the user which in this case, it would make sense for each product (object)
    # created, to return the name of it (Which the user gave it in the form in our example).
