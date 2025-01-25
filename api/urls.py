from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegistrationView,
    MembershipViewSet,
    DocumentViewSet,
    SavingsPlanViewSet,
    ContributionViewSet,
    AuditLogViewSet,
)

router = DefaultRouter()
router.register('memberships', MembershipViewSet)
router.register('documents', DocumentViewSet)
router.register('savings-plans', SavingsPlanViewSet)
router.register('contributions', ContributionViewSet)
router.register('audit-logs', AuditLogViewSet)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]
