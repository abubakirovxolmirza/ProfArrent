from django.urls import path
from .views import CreateUserView, UserListView, AdminListView, CreateAdminView, ModeratorListView, CreateModeratorView, UserDetailView, AdminDetailView, LoginView, ModeratorDetailView
urlpatterns = [
    path('user/', CreateUserView.as_view(), name='register'),
    path('admin/', CreateAdminView.as_view(), name='create-admin'),
    path('moderator/', CreateModeratorView.as_view(), name='create-moderator'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('admins/<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),
    path('moderators/<int:pk>/', ModeratorDetailView.as_view(), name='moderator-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('admins/', AdminListView.as_view(), name='admin-list'),
    path('moderators/', ModeratorListView.as_view(), name='moderator-list'),
]
