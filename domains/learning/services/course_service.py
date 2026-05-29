from django.db import transaction
from django.http import Http404
from domains.learning.models import Course


def list_courses():
    return Course.objects.all()


def filter_courses(**kwargs):
    return Course.objects.filter(**kwargs)


def get_courses_by_id(course_id):
    if not course_id:
        raise Http404("Course not found")

    try:
        return Course.objects.get(
            id=course_id
        )

    except Course.DoesNotExist:
        raise Http404("Course not found")

@transaction.atomic
def delete_course(course_id):
    obj = get_courses_by_id(course_id)
    obj.delete()
    return True
