from django.db import transaction
from django.http import Http404
from domains.work.models import Assignment


def list_assignments():
    return Assignment.objects.all()


def filter_assignments(**kwargs):
    return Assignment.objects.filter(**kwargs)


def get_assignment_by_id(assignment_id):
    if not assignment_id:
        raise Http404("Assignment not found")

    try:
        return Assignment.objects.get(
            id=assignment_id
        )

    except Assignment.DoesNotExist:
        raise Http404("Assignment not found")

@transaction.atomic
def delete_assignment(assignment_id):
    obj = get_assignment_by_id(assignment_id)
    obj.delete()
    return True
