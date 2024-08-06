from django.urls import path

from users.views import (
    RoleCreateView,
    RoleDeleteView,
    RoleListView,
    RoleUpdateView
)

urlpatterns = [
    path(
        route='role/',
        view=RoleListView.as_view(),
        name='role_list'
    ),
    path(
        route='role/create',
        view=RoleCreateView.as_view(),
        name='role_create'
    ),
    path(
        route='role/<int:id>',
        view=RoleUpdateView.as_view(),
        name='role_update'
    ),
    path(
        route='role/delete/<int:id>',
        view=RoleDeleteView.as_view(),
        name='role_delete'
    )
]