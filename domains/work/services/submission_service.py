from django.db import transaction
from django.http import Http404
from domains.work.models import Submission


def list_submissions():
    return Submission.objects.all()


def filter_submissions(**kwargs):
    return Submission.objects.filter(**kwargs)


def get_submission_by_id(submission_id):
    if not submission_id:
        raise Http404("Enrollment not found")

    try:
        return Submission.objects.get(
            id=submission_id
        )

    except Submission.DoesNotExist:
        raise Http404("Submission not found")

@transaction.atomic
def grade_submission(submission_id, grade, feedback):
    submission = get_submission_by_id(submission_id)
    submission.graded = True
    submission.grade = grade
    submission.feedback = feedback
    submission.save()
    return submission

