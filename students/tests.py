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

    def test_student_creation(self):
        group = Group.objects.create(name='Test')

        Student.objects.create(
            first_name='f_name', last_name='l_name',surname='surename',
            card_number='1234567890', date_birthday='1987-3-3',
            group=group
        )

        self.assertEqual(Student.objects.all().count(), 1)



# class SimpleTest(ClientTest):
#
#
#     fixtures = ['fixtures/initial_data.json']
#
#     def test_functions(self):
#         # проверка на возможность логинится
#         login = self.client.login(username='moma', password='415823')
#         self.failUnless(login, 'Could not log in')
#
#         # добавление группы
#         data_group = {'name': 'Abc', 'elder': ''}
#         self.POST('/group_create/', data_group, status=302)
#
#         # добавление студента в группу
#         group_list = Group.objects.all()
#         group_id = 0
#         for g in group_list:
#             if g.id > group_id:
#                 group_id = g.id
#         data_student = {'first_name': 'AAAA',
#                         'last_name': 'bbbbb',
#                         'surname': 'cccc',
#                         'date_birthday': '1987-3-3',
#                         'card_number': '5555',
#                         'group': group_id, }
#         print(group_id)
#         self.POST('/student_create/', data_student, status=302)
#
