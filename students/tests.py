from django.test import TestCase
from students.models import Group, Student
from django.test import Client

# Create your tests here.


class ClientTest(TestCase):
    """
    Small test suite to demonstrate helper methods.
    You'd probably want to abstract these to your own subclass
    of django.test.TestCase so you could import and use it in
    each of your tests.py files.
    """

    def GET(self, url, status=200, mimetype="text/html"):
        """Get a URL and require a specific status code before proceeding"""
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, status)
        self.failUnless(response.__getitem__('Content-Type').startswith(mimetype))
        return response

    def POST(self, url, params, status=200, mimetype="text/html"):
        """Make a POST and require a specific status code before proceeding"""
        response = self.client.post(url, params)
        self.failUnlessEqual(response.status_code, status)
        self.failUnless(response.__getitem__('Content-Type').startswith(mimetype))
        return response


class SimpleTest(ClientTest):


    fixtures = ['fixtures/initial_data.json']

    def test_functions(self):
        # проверка на возможность логинится
        login = self.client.login(username='moma', password='415823')
        self.failUnless(login, 'Could not log in')

        # добавление группы
        data_group = {'name': 'Abc', 'elder': ''}
        self.POST('/group_create/', data_group, status=302)

        # добавление студента в группу
        group_list = Group.objects.all()
        group_id = 0
        for g in group_list:
            if g.id > group_id:
                group_id = g.id
        data_student = {'first_name': 'AAAA',
                        'last_name': 'bbbbb',
                        'surname': 'cccc',
                        'date_birthday': '1987-3-3',
                        'card_number': '5555',
                        'group': group_id, }
        print(group_id)
        self.POST('/student_create/', data_student, status=302)

