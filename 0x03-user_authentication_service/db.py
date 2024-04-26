#!/usr/bin/env python3
"""DB module
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from sqlalchemy.exc import InvalidRequestError


DATA = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']

class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database.

        Args:
            email (str): The user's email.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The added User object.
        """
        if not email or not hashed_password:
            return
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user
    
    def find_user_by(self, **kwargs) -> User:
        """find user by some arguments
        Arg:
            **kwargs: Known arguments
        Returns:
            User: user found or raise error
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user
    
    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user

        Args:
            user_id (int): id of user
        """
        user = self.find_user_by(id=user_id)
        for key, val in kwargs.items():
            if key not in DATA:
                raise ValueError
            setattr(user, key, val)
        self._session.commit()
        return None
