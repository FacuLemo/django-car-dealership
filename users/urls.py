from django.urls import path

from users.views.role_views import (
    RoleCreateView,
    RoleDeleteView,
    RoleListView,
    RoleUpdateView,
)
from users.views.user_roles_views import (
    UserRolesCreateView,
    UserRolesDeleteView,
    UserRolesListView,
    UserRolesUpdateView,
)
from users.views.user_views import UserProfileView

urlpatterns = [
    path(
        route="<int:id>",
        view=UserProfileView.as_view(),
        name="user_profile",
    ),
    path(
        route="role/",
        view=RoleListView.as_view(),
        name="role_list",
    ),
    path(
        route="role/create",
        view=RoleCreateView.as_view(),
        name="role_create",
    ),
    path(
        route="role/<int:id>",
        view=RoleUpdateView.as_view(),
        name="role_update",
    ),
    path(
        route="role/delete/<int:id>",
        view=RoleDeleteView.as_view(),
        name="role_delete",
    ),
    path(
        route="user_role/",
        view=UserRolesListView.as_view(),
        name="user_role_list",
    ),
    path(
        route="user_role/create",
        view=UserRolesCreateView.as_view(),
        name="user_role_create",
    ),
    path(
        route="user_role/<int:id>",
        view=UserRolesUpdateView.as_view(),
        name="user_role_update",
    ),
    path(
        route="user_role/delete/<int:id>",
        view=UserRolesDeleteView.as_view(),
        name="user_role_delete",
    ),
]
