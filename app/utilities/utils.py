from pydantic import ValidationError


def success_response(*, data, code):
    return {"data": data.dict()}, code


def success_response_multi(*, data, code):
    return {"data": [item.dict() for item in data]}, code


def validation_error_reponse(*, error: ValidationError, code):
    return {
        "errors": [{"field": e["loc"][0], "msg": e["msg"]} for e in error.errors()]
    }, code


def error_response(*, error, code):
    return {"errors": {"msg": error}}, code
