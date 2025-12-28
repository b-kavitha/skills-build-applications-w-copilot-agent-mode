"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""octofit_tracker URL Configuration"""

from django.contrib import admin
from django.urls import path, include
import os

# Get Codespace name dynamically
CODESPACE_NAME = os.environ.get('CODESPACE_NAME', 'localhost')
BASE_URL = f"https://{CODESPACE_NAME}-8000.app.github.dev"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    #path('api/users/', include('users.urls')),        # users app
    #path('api/activities/', include('activities.urls')),  # activities app
    #path('api/teams/', include('teams.urls')),       # teams app
    #path('api/leaderboard/', include('leaderboard.urls')), # leaderboard app
    #path('api/workouts/', include('workouts.urls')), # workouts app
]

# Optional: you can print BASE_URL for debugging
print(f"API Base URL: {BASE_URL}")

