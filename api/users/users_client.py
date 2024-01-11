import logging

import api.users.users_test_data as users_test_data
import api.users.users_mgmt as users_mgmt
import json


def create_user(**kwargs) -> tuple:
    create_user_payload = users_test_data.create_user_payload(username=kwargs['username'], email=kwargs['email'])
    result = users_mgmt.create_user(create_user_payload, **kwargs)
    created_user_data = json.loads(result.text)
    return created_user_data['name'], created_user_data['id']


def get_users():
    users_list = users_mgmt.get_users().json()
    if not users_list:
        logging.exception("No users were found")
    else:
        logging.info(f'{len(users_list)} users were found')
    return users_list


def get_user_id_by_username(**kwargs):
    username = kwargs['username']
    users_list = get_users()
    user_id = [user_data for user_data in users_list if username == user_data['name']]
    return user_id


def get_user_by_id(**kwargs):
    return users_mgmt.get_users_by_id(user_id=kwargs['user_id'])

def delete_user(**kwargs):
    return users_mgmt.delete_user(user_id=kwargs['user_id'])
