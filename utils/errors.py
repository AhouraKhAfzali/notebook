def get_error_message(error):

    if hasattr(error, "message_dict"):
        return next(
            iter(error.message_dict.values())
        )[0]

    if hasattr(error, "messages"):
        return error.messages[0]

    return str(error)
