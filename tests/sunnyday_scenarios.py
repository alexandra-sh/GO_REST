import logging
from http import HTTPStatus
import api.users.users_client as users_client
import api.constants as constants


def test_get_users():
    logging.info("Get users test scenario STARTED")
    users_client.get_users()
    logging.info("Get users test scenario FINISHED")


def test_get_user_details():
    logging.info("Get user details test scenario STARTED")
    new_user_name, new_user_id = users_client.create_user(username=constants.NEW_USER_NAME, email=constants.NEW_USER_EMAIL)
    users_client.get_user_by_id(user_id=new_user_id)
    logging.info("Get user details test scenario FINISHED")


def test_active_user_creation():
    logging.info("Create new user test scenario STARTED")
    new_user_name, new_user_id = users_client.create_user(username=constants.NEW_USER_NAME, email=constants.NEW_USER_EMAIL)
    logging.info(f'New user {new_user_name} with id {new_user_id} was created successfully')
    logging.info("Create new user test scenario FINISHED")


def test_delete_user():
    logging.info("Create delete user test scenario STARTED")
    new_user_name, new_user_id = users_client.create_user(username=constants.NEW_USER_NAME, email=constants.NEW_USER_EMAIL)
    delete_user_response_code = users_client.delete_user(user_id=new_user_id)
    if delete_user_response_code == HTTPStatus.NO_CONTENT:
        logging.info(f'The user {new_user_name} with id {new_user_id} was deleted successfully')
    else:
        logging.warning(f'The user {new_user_name} with id {new_user_id} delete operation failed with HTTP code {delete_user_response_code}')
    logging.info("Create delete user test scenario FINISHED")