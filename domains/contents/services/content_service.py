from django.db import transaction
from django.http import Http404
from domains.contents.models import Contents

def list_contents():
    return Contents.objects.all()


def filter_contents(**kwargs):
    return Contents.objects.filter(**kwargs)


def get_content_by_id(content_id):
    if not content_id:
        raise Http404("Content not found")

    try:
        return Contents.objects.get(
            id=content_id
        )

    except Contents.DoesNotExist:
        raise Http404("Content not found")

@transaction.atomic
def delete_content(content_id):
    obj = get_content_by_id(content_id)
    obj.delete()
    return True
