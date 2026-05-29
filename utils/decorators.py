from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import redirect
from .errors import get_error_message


def handle_service_errors():

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            try:
                return view_func(
                    request,
                    *args,
                    **kwargs
                )

            except Http404:
                raise

            except ValidationError as e:

                messages.error(
                    request,
                    get_error_message(e)
                )

                return redirect(
                    request.META.get(
                        "HTTP_REFERER"
                    )
                )

        return wrapper

    return decorator
