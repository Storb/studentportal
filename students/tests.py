from django.core.urlresolvers import reverse
from django.test import TestCase


class RegisterTest(TestCase):

    def test_creation(self):
        resp = self.client.post(reverse('register_user'),
                                data={'username': 'user',
                                      'email': 'user@test.com',
                                      'password1': '123',
                                      'password2': '123'})
        self.assertRedirects(resp, reverse('register_success'))


class LoginUserTest(TestCase):

    def login_user(self):
        import ipdb;ipdb.set_trace()
        login = self.client.login(username='user', password='123')
        self.assertEqual(login, True)


class GroupCreateTest(TestCase):

    def group_creation(self):
        resp = self.client.post(reverse('group_create'),
                                data={'name':'group'})
        self.assertEqual(resp, True)


class StudentCreateTest(TestCase):

    def student_creation(self):

        resp = self.client.post(reverse('student_create'),
                                data={'first_name': 'f_name',
                                      'last_name': 'l_name',
            'surname':'surename', 'card_number': '1234567890',
            'date_birthday': '1987-3-3', 'group':'group'})

        self.assertEqual(resp, True)


# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)
#
#
# class StudentsSimpleTest(TestCase):
#     def test_index(self):
#         url = reverse("student_create")
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)

