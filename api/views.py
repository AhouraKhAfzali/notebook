# django imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
# model imports
from domains.academia.models import Institution, Subject
from accounts.models import User

# Create your views here.
@api_view(['GET'])
def autocomplete_institution(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        objects = Institution.objects.filter(name__icontains=query)[:5]
        results = [{"id": i.id, "name": i.name} for i in objects]
    return Response(results)

@api_view(['GET'])
def autocomplete_major(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        objects = Subject.objects.filter(name__icontains=query)[:5]
        results = [{"id": i.id, "name": i.name} for i in objects]
    return Response(results)

@api_view(['GET'])
def autocomplete_teacher(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        objects = User.objects.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query),
            role="teacher"
        )[:5]
        results = [{"id": i.id, "name": f"{i.first_name} {i.last_name}" } for i in objects]
    return Response(results)
