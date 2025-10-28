import random
from datetime import timedelta, date
from django.utils import timezone
from django.contrib.auth.models import User
from app.models import Project, Task, Notification  # ← غيّر myapp لاسم التطبيق عندك

# ========== إنشاء مستخدمين ==========
if User.objects.count() == 0:
    print("🔹 Creating users...")
    for i in range(5):
        User.objects.create_user(
            username=f'user{i+1}',
            email=f'user{i+1}@example.com',
            password='password123'
        )

users = list(User.objects.all())

# ========== إنشاء مشاريع ==========
print("🔹 Creating projects...")
for i in range(10):
    owner = random.choice(users)
    project = Project.objects.create(
        name=f'Project {i+1}',
        owner=owner
    )

# ========== إنشاء مهام ==========
print("🔹 Creating tasks...")
projects = list(Project.objects.all())
for i in range(50):
    project = random.choice(projects)
    Task.objects.create(
        project=project,
        title=f'Task {i+1}',
        description=f'This is the description for task {i+1}',
        completed=random.choice([True, False]),
        due_date=date.today() + timedelta(days=random.randint(1, 30))
    )

# ========== إنشاء إشعارات ==========
print("🔹 Creating notifications...")
for i in range(20):
    user = random.choice(users)
    Notification.objects.create(
        user=user,
        message=f'Notification message {i+1} for {user.username}',
    )

print("✅ Done seeding data!")
