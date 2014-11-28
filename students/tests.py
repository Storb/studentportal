from django.core.urlresolvers import reverse
from django.test import TestCase
from students.models import Group

class RegisterTest(TestCase):

    def test_creation(self):
        resp = self.client.post(reverse('register_user'),
                                data={'username': 'user',
                                      'email': 'user@test.com',
                                      'password1': '123',
                                      'password2': '123'})
        self.assertRedirects(resp, reverse('register_success'))

        login = self.client.login(username='user', password='123')
        self.assertEqual(login, True)


class GroupCreateTest(TestCase):

    def test_group_creation(self):
        resp = self.client.post(reverse('group_create'), data={'name':'group'})
        self.assertRedirects(resp, reverse('group_detail', args=[1, ]))


class StudentCreateTest(TestCase):
    def test_student_creation(self):
        group = Group.objects.create(name='name')
        resp = self.client.post(reverse('student_create'),
                                data={'first_name': 'f_name', 'last_name': 'l_name',
                                      'surname':'surname', 'card_number': '1234567890',
                                      'date_birthday': '1987-3-3', 'group': group.id})

        self.assertRedirects(resp, reverse('student_detail', args=[1, ]))


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

