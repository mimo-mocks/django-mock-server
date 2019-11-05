import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from mocks.models import Mock, HeaderType, HttpVerb
from mocks.serializers import MockSerializer, HeaderTypeSerializer, HttpVerbSerializer
from mocks.services import MocksFetchService

# Create your views here.


@csrf_exempt  # This allows verbs besides GET
def fetch_mock(request):
    query_params = {**request.GET.dict(), **request.POST.dict()}
    mock_route = request.path.rstrip('/')

    mock = MocksFetchService.get_by_route_and_verb(mock_route, request.method, query_params)

    content = json.loads(mock.content)
    status_code = int(mock.status_code)

    response = JsonResponse(
        content,
        status=status_code,
        safe=False
    )
    for header in mock.header_set.all():
        header_type, value = header.as_response_header
        response[header_type] = value

    return response


class MockViewset(viewsets.ModelViewSet):
    queryset = Mock.objects.all()
    serializer_class = MockSerializer


class HeaderTypeViewset(viewsets.ModelViewSet):
    queryset = HeaderType.objects.all()
    srializer_class = HeaderTypeSerializer


class HttpVerbViewset(viewsets.ModelViewSet):
    queryset = HttpVerb.objects.all()
    srializer_class = HttpVerbSerializer