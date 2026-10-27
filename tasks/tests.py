from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskFlowTests(TestCase):
    def test_create_toggle_delete(self):
        self.assertEqual(self.client.get(reverse('index')).status_code, 200)
        self.client.post(reverse('index'), {'title': 'یادگیری جنگو'})
        task = Task.objects.get()
        self.assertContains(self.client.get(reverse('index')), 'یادگیری جنگو')
        self.client.post(reverse('toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.client.post(reverse('delete', args=[task.pk]))
        self.assertFalse(Task.objects.exists())

    def test_invalid_titles(self):
        for title in ['', '   ', 'a' * 201]:
            self.client.post(reverse('index'), {'title': title})
        self.assertFalse(Task.objects.exists())

    def test_mutations_require_post_and_csrf(self):
        task = Task.objects.create(title='test')
        for name in ['toggle', 'delete']:
            url = reverse(name, args=[task.pk])
            self.assertEqual(self.client.get(url).status_code, 405)
            self.assertEqual(Client(enforce_csrf_checks=True).post(url).status_code, 403)

    def test_missing_task(self):
        self.assertEqual(self.client.post(reverse('toggle', args=[999])).status_code, 404)
