from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date
from app.models import Project, Task, Notification

User = get_user_model()


class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.project = Project.objects.create(
            name="Test Project",
            owner=self.user
        )

    def test_project_str(self):
        """__str__ should return project name"""
        self.assertEqual(str(self.project), "Test Project")

    def test_project_owner_relation(self):
        """Project should be linked to the correct owner"""
        self.assertEqual(self.project.owner.username, "testuser")


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.task = Task.objects.create(
            project=self.project,
            title="Test Task",
            description="This is a test task",
            due_date=date(2025, 12, 31)
        )

    def test_task_str_pending(self):
        """__str__ should show task title with (pending)"""
        self.assertEqual(str(self.task), "Test Task (pending)")

    def test_task_str_done(self):
        """__str__ should show (done) when completed=True"""
        self.task.completed = True
        self.task.save()
        self.assertEqual(str(self.task), "Test Task (done)")

    def test_task_default_completed_is_false(self):
        """completed field should default to False"""
        self.assertFalse(self.task.completed)

    def test_task_project_relation(self):
        """Task should belong to the correct project"""
        self.assertEqual(self.task.project, self.project)
        self.assertEqual(self.project.tasks.count(), 1)


class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.notification = Notification.objects.create(
            user=self.user,
            message="You have a new task assigned!"
        )

    def test_notification_str(self):
        """__str__ should include user and creation date"""
        expected_str_start = f"Notification for {self.user}"
        self.assertTrue(str(self.notification).startswith(expected_str_start))

    def test_notification_user_relation(self):
        """Notification should be linked to the correct user"""
        self.assertEqual(self.notification.user, self.user)
