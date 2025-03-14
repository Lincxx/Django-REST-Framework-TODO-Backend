from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='first todo', body='todo body')

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'first todo')
        self.assertEqual(self.todo.body, 'todo body')
        self.assertEqual(str(self.todo), 'first todo')
