# coding=utf8
from __future__ import unicode_literals

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from willie.tools import Nick

Base = declarative_base()


class UserId(Base):
    __tablename__ = 'nick_ids'
    nick_id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = 'nicknames'

    nick_id = Column(Integer, ForeignKey('nick_ids.nick_id'))
    slug = Column(String, primary_key=True)
    canonical = Column(String)

    def __init__(self, nick_id, nick):
        self.nick_id = nick_id
        self.nick = nick
        self.slug = Nick(nick).lower()

    def __repr__(self):
        return ("<Nick(nick_id={}, slug='{}', canonical='{}'".format(
                self.nick_id, self.slug, self.canonical))


class UserData(Base):
    __tablename__ = 'nick_values'

    nick_id = Column(Integer, ForeignKey('nick_ids.nick_id'))
    key = Column(String, primary_key=True)
    value = Column(String)

    def __repr__(self):
        return ("<UserData(nick_id={}, key='{}', canonical='{}'".format(
                self.nick_id, self.key, self.canonical))


class ChannelData(Base):
    __tablename__ = 'channel_values'

    channel = Column(String, primary_key=True)
    key = Column(String, primary_key=True)
    value = Column(String)

def get_session(db):
    engine = create_engine(db.get_url())
    Session = sessionmaker(bind=engine)
    return Session()
