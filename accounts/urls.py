from django.conf.urls import url
from .views import LoginView, LogoutView, UserView
from rest_framework.authtoken import views


app_name="accounts"

urlpatterns=[
	url(r'^login/$',LoginView.as_view()),
	url(r'^logout/$',LogoutView.as_view()),
	url(r'^token-auth/', views.obtain_auth_token),
	url(r'^me/',UserView.as_view())
]