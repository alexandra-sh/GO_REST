import requests
from http import HTTPStatus
import api.constants as constants


def create_user(payload, status_code=HTTPStatus.OK, check_response: bool = False, **kwargs):
    response = requests.post(constants.USERS, data=payload, headers={'Authorization': constants.AUTH_TOKEN})
    if check_response:
        _check_response_status_code(response.status_code, status_code)
    return response


def get_users(status_code=HTTPStatus.OK, check_response: bool = False, **kwargs):
    response = requests.get(f'{constants.USERS}/{constants.MAX_USERS}')
    if check_response:
        _check_response_status_code(response.status_code, status_code)
    return response


def get_users_by_id(user_id, status_code=HTTPStatus.OK, check_response: bool = False, **kwargs):
    response = requests.get(f'{constants.USERS}/{user_id}')
    if check_response:
        _check_response_status_code(response.status_code, status_code)
    return response


def delete_user(user_id, status_code=HTTPStatus.NO_CONTENT, check_response: bool = True, **kwargs):
    response = requests.delete(f'{constants.USERS}/{user_id}', headers={'Authorization': constants.AUTH_TOKEN})
    if check_response:
        _check_response_status_code(response.status_code, status_code)
    return response.status_code


def _check_response_status_code(response_status_code, status_code):
    if response_status_code != status_code:
        raise AssertionError (f'response status code {response_status_code} is not the expected status code {status_code}')


