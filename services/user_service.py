from datetime import datetime
from typing import Optional, List
from datetime import datetime

import data.__db_session as db_session
from data.users import User




def get_user_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(User).count()
    finally:
        session.close()

def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    try:
        return session.query(User).filter(User.email == email).first()
    finally:
        session.close()


def create_user(email: str, google_sub_id: str ) -> Optional[User]:

    if find_user_by_google_sub_id(google_sub_id):
        return None

    user = User()
    user.email = email
    user.google_sub_id = google_sub_id
    user.created_date=datetime.now()

    session = db_session.create_session()

    try:
        session.add(user)
        session.commit()
    finally:
        session.close()

    return user

def find_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    finally:
        session.close()

def find_user_by_google_sub_id(google_sub_id) -> Optional[User]:
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.google_sub_id == google_sub_id).first()
        return user
    finally:
        session.close()