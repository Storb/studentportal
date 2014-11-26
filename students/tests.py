from django.core.urlresolvers import reverse
from django.test import TestCase
from students.models import Group, Student


# Create your tests here.


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class StudentsSimpleTest(TestCase):
    def test_index(self):
        url = reverse("student_create")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class GroupTest(TestCase):

    def test_creation(self):
        resp = self.client.post(reverse('register_user'),
                                data={'username': 'user',
                                      'email': 'user@test.com',
                                      'password1': '123',
                                      'password2': '123'})
        self.assertRedirects(resp, reverse('register_success'))

        login = self.client.login(username='user', password='123')
        self.assertEqual(login, True)

        group = Group.objects.create(name='Test')

        Student.objects.create(
            first_name='f_name', last_name='l_name',
            surname='surename', card_number='1234567890',
            date_birthday='1987-3-3', group=group
        )

        self.assertEqual(Student.objects.all().count(), 1)
