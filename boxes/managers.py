from django.db import models


class MessagesQueryset(models.QuerySet):
    def archived(self):
        return self.filter(archived=True)

    def not_archived(self):
        return self.filter(archived=False)


class MessagesManager(models.Manager):
    def get_queryset(self):
        return MessagesQueryset(self.model, using=self._db)

    def archived(self):
        return self.get_queryset().archived()

    def not_archived(self):
        return self.get_queryset().not_archived()
