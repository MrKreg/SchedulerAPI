from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from app.pkg.info.models import Term
from app.pkg.scheduler.models import Schedule


class SchedulerViewSet(GenericViewSet):
    serializer_class = Schedule
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        term = Term.objects.current()
        return Schedule.objects.filter(info__term=term)

    @action(methods=['get'], detail=False)
    def today(self, request):
        pass
