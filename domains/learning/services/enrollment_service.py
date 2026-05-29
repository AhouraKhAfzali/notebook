from django.http import Http404
from domains.learning.models import Enrollment, Course
from django.db import transaction, IntegrityError
from django.core.exceptions import ValidationError
from .course_service import get_courses_by_id


def filter_enrollments(**kwargs):
    return Enrollment.objects.filter(**kwargs)


def get_enrollments_by_id(enrollment_id):
    if not enrollment_id:
        raise Http404("Enrollment not found")

    try:
        return Enrollment.objects.get(
            id=enrollment_id
        )

    except Enrollment.DoesNotExist:
        raise Http404("Enrollment not found")


@transaction.atomic
def create_enrollment(student, course_obj_id, **kwargs):
    course_obj = get_courses_by_id(course_obj_id)
    try:
        return Enrollment.objects.create(
            student=student,
            course_obj=course_obj,
            **kwargs
        )

    except IntegrityError:
        raise ValidationError({
            "student": "Enrollment already exists"
        })


@transaction.atomic
def accept_enrollment(enrollment_id, **kwargs):
    enrollment = get_enrollments_by_id(enrollment_id)
    enrollment.course_obj.students.add(enrollment.student)
    enrollment.status = "accepted"
    enrollment.save()
    return enrollment


@transaction.atomic
def reject_enrollment(enrollment_id, **kwargs):
    enrollment = get_enrollments_by_id(enrollment_id)
    enrollment.status = "rejected"
    enrollment.save()
    return enrollment







# def create_enrollment(student, course_obj_id, **kwargs):
#     print(student, course_obj_id)
    # if filter_enrollments(student=student, course_obj_id=course_obj_id, status="pending") or filter_enrollments(student=student, course_obj_id=course_obj_id, status="accepted"):
    #     raise ValidationError("Enrollment already exists")
    # try:
    # obj = Enrollment(student=student, course_obj_id=course_obj_id, **kwargs)
    # obj.full_clean()
    # obj.save()
    # return obj
    # except ValidationError as e:
    # if obj.full_clean():
    # return False
    # check_enrollment = Enrollment.objects.filter(
    #     Q(student=student, course_obj_id=course_obj_id, status="pending") |
    #     Q(student=student, course_obj_id=course_obj_id, status="approved"),
    # )
    # if not check_enrollment:
    #     object = Enrollment.objects.create(student=student, course_obj_id=course_obj_id)
    #     return object
    # else:
    #     raise ValidationError("شما قبلا درخواست ثبت نام برای این کلاس را ثبت کرده اید.")







    # obj = Enrollment(student=student, course_obj_id=course_obj_id, **kwargs)
    # obj.full_clean()
    # with transaction.atomic():
    #     obj.save()
    # return obj







    # obj = Enrollment.objects.filter(id=enrollment_id).first()
    # if not obj:
    #     raise ValidationError({"id": "Enrollment not found"})
    # return obj