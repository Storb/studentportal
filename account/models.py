from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Contact(User):

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})