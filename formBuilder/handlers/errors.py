from flask import jsonify


def error_response(status_code, message=None):
    payload = {'error': status_code, 'message': message or 'An error occurred'}
    response = jsonify(payload)
    response.status_code = status_code
    return response


def not_found_error(error):
    return error_response(404, error.description or "Resource not found")


def bad_request_error(error):
    return error_response(400, error.description or "Bad request")


def internal_error(error):
    return error_response(500, error.description or "Internal server error")


def register_error_handlers(app):
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(400, bad_request_error)
    app.register_error_handler(500, internal_error)
