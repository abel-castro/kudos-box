from django.db import models


class Member(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Box(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    members = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return self.name


CARD_COLOR_CHOICES = [
    ("BLUE", "Blue"),
    ("RED", "Red"),
    ("YELLOW", "Yellow"),
    ("GREEN", "Green"),
    ("BLACK", "Black"),
    ("DEFAULT", "Default"),
]


class Message(models.Model):
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    box = models.ForeignKey(Box, on_delete=models.DO_NOTHING)
    card_color = models.CharField(
        choices=CARD_COLOR_CHOICES, default="DEFAULT", max_length=10
    )
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.box}: {self.text}"

    def get_card_css_classes(self) -> str:
        """
        Return the css classes for the bootstrap card.

        https://getbootstrap.com/docs/5.0/components/
        card/#card-styles
        """
        if self.card_color == "BLUE":
            return "text-white bg-primary"
        elif self.card_color == "RED":
            return "text-white bg-danger"
        elif self.card_color == "YELLOW":
            return "bg-warning"
        elif self.card_color == "GREEN":
            return "text-white bg-success"
        elif self.card_color == "BLACK":
            return "text-white bg-dark"
        else:
            return ""
