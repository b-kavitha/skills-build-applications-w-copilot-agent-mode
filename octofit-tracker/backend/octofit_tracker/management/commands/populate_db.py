from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        app_models.Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        app_models.Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        app_models.Activity.objects.create(user=clark, type='run', duration=50, calories=450)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=30)
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=45)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=tony, points=1000)
        app_models.Leaderboard.objects.create(user=steve, points=900)
        app_models.Leaderboard.objects.create(user=bruce, points=950)
        app_models.Leaderboard.objects.create(user=clark, points=980)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
