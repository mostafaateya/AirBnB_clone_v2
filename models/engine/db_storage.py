#!/usr/bin/python3
"""
DB_storage module
"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class DBStorage:
    """
    DBStorgae class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initializations.
        """

        dialect = 'mysql'
        driver = 'mysqldb'
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        conn = "{}+{}://{}:{}@{}/{}".format(
                dialect,
                driver,
                user,
                password,
                host,
                database)
        self.__engine = create_engine(conn, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        if cls=None, query all types of objects
        """

        dic = {}
        if cls is None:
            objects_list = self.__session.query(User).all()
            objects_list.extend(self.__session.query(State).all())
            objects_list.extend(self.__session.query(City).all())
            objects_list.extend(self.__session.query(Amenity).all())
            objects_list.extend(self.__session.query(Place).all())
            objects_list.extend(self.__session.query(Review).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objects_list = self.__session.query(cls).all()

        for obj in objects_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            dic[key] = obj
        return (dic)

    def new(self, obj):
        """
        Adds the obj to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves changes to the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        - create all tables in the database
        - create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """
        closes the session
        """
        self.__session.close()
