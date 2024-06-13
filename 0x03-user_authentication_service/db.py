#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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
        """Add a user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The created user object.
        """
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments.

        Args:
            kwargs (dict): Arbitrary keyword arguments for filtering the users.

        Returns:
            User: The first user found based on the filter criteria.

        Raises:
            NoResultFound: If no user is found.
            InvalidRequestError: If invalid arguments are provided.
        """
        session = self._session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("Given criteria no user was found.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes based on keyword arguments.

        Args:
            user_id (int): The ID of the user to update.
            kwargs (dict): Represents the attributes to update.

        Returns:
            None

        Raises:
            ValueError: If an argument does not correspond to a user attribute.
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError()

        session = self._session
        session.commit()
