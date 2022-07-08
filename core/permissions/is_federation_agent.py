
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsFederationAgent(IsAuthenticated):
    message = 'You don\'t have federation agent access.'

    def has_permission(self, request: Request, view):
        return super().has_permission(request, view) and request.user.is_federation_agent


class IsFederationAgentOrReadOnly(IsFederationAgent):
    message = 'You don\'t have federation agent access.'

    def has_permission(self, request: Request, view):
        return request.method in SAFE_METHODS or super().has_permission(request, view)
