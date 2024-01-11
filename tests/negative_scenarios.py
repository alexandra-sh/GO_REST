from http import HTTPStatus
import api.users.users_client as users_client
import logging


def test_create_already_existing_user():
    logging.info("Already existing user creation test scenario STARTED")
    try:
        any_existing_user = users_client.get_users()[0]
        any_existing_user_id = any_existing_user['id']
        any_existing_user_name = any_existing_user['name']
        any_existing_user_email = any_existing_user['email']
        logging.info(f'Found aleardy existing user {any_existing_user_name} with id: {any_existing_user_id}, email: '
                     f'{any_existing_user_email}')
        response = users_client.create_user(username=any_existing_user_name, email=any_existing_user_email,
                                            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, check_response=True)
        logging.error(
            f'Already existing user creation failed with HTTP status code:{response.status_code} and message: {response.text}')
    except IndexError:
        logging.error("Any existing user was not found")
    finally:
        logging.info("Already existing user creation test scenario FINISHED")
