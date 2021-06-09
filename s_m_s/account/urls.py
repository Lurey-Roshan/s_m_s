from django.urls import path
from account.views import *

urlpatters = [
	path('profile/', profile, name='profile'),
	path('update/', update_profile, name='update-profile')

]