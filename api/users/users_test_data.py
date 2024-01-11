def create_user_payload(username, email, gender="male", status="active"):
    return {"name": username, "email": email, "gender": gender, "status": status}