# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_psql.ipynb (unless otherwise specified).

__all__ = ['branch', 'port', 'engine', 'Session', 'session', 'Base', 'schema', 'LocalBase', 'Foods', 'Users', 'Dishes',
           'User_properties', 'FoodsP', 'FoodsPI', 'Indexed']

# Cell
import sys
sys.path.insert(0,'..')
from mytools.psql import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String, Text, Float, Boolean, ForeignKey, and_, or_, MetaData
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import update
from sqlalchemy import desc
import pandas as pd
import datetime
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import select, exists
from IPython.display import clear_output
from sqlalchemy import Column, Integer, String ,DateTime,UniqueConstraint,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql.sqltypes import *
from sqlalchemy import *
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Executable, ClauseElement #_literal_as_text
from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement
from sqlalchemy.inspection import inspect
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import VARCHAR

from sqlalchemy.dialects.postgresql import JSON

from sqlalchemy.dialects.postgresql import REAL

from sqlalchemy import cast

from .paths import branch
print(branch)

# Cell

branch = 'prod'

port = 5434 if branch == 'prod' else 5432


engine = create_engine(f'postgresql+psycopg2://postgres:KJnbuiwuef89k@localhost/postgres?port={port}',pool_size=64) #dev engine
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Cell
schema = 'food'
LocalBase = declarative_base(metadata=MetaData(schema=schema))

# Cell
class Foods (LocalBase):
    __tablename__ = 'foods'
    id                  = Column(BIGINT, primary_key=True)
    description         = Column(String,          nullable=False)
    category            = Column(String,          nullable=False)
    energy              = Column(Float,          nullable=False)
    protein             = Column(Float,          nullable=False)
    carb                = Column(Float,          nullable=False)
    fat                 = Column(Float,          nullable=False)

    clip                = Column(ARRAY(REAL),          nullable=True)

# Cell
class Users (LocalBase):
    __tablename__ = 'users'
    id                  = Column(BIGINT,     primary_key=True)
    first_name          = Column(String,     nullable=True)
    last_name           = Column(String,     nullable=True)
    username            = Column(String,     nullable=True)
    language_code       = Column(String,     nullable=True)


# Cell
class Dishes (LocalBase):
    __tablename__ = 'dishes'
    id                   = Column(BIGINT,  primary_key=True, autoincrement = True)
    description          = Column(String,   nullable=False)
    energy               = Column(Float,    nullable=False)
    protein              = Column(Float,    nullable=False)
    carb                 = Column(Float,    nullable=False)
    fat                  = Column(Float,    nullable=False)
    score                = Column(Float,    nullable=False)

    photo_id            = Column(String,   nullable=False)
    user_id             = Column(BIGINT,   nullable=False)
    photo_message_id    = Column(BIGINT,   nullable=False)
    message_id          = Column(BIGINT,   nullable=False)

    timestamp           = Column(DateTime(timezone=True), nullable=False)
    ml_version          = Column(Float,    nullable=False)

    grams               = Column(Float,    nullable=True)

# Cell
class User_properties (LocalBase):
    __tablename__ = 'user_properties'
    id                  = Column(BIGINT,  primary_key=True, autoincrement = True)
    user_id             = Column(BIGINT,   nullable=False)
    property            = Column(String,   nullable=False)
    value               = Column(String,   nullable=False)
    timestamp           = Column(DateTime(timezone=True), nullable=False)

# Cell
class FoodsP (LocalBase):
    __tablename__ = 'foods_prompted' #inferenced text of altered food classes
    id                  = Column(BIGINT, primary_key=True)
    description         = Column(String,          nullable=False)
    category            = Column(String,          nullable=False)
    energy              = Column(Float,           nullable=False)
    protein             = Column(Float,           nullable=False)
    carb                = Column(Float,           nullable=False)
    fat                 = Column(Float,           nullable=False)
    text                = Column(String,          nullable=False)

    clip                = Column(ARRAY(REAL),          nullable=True)

# Cell
class FoodsPI (LocalBase):
    __tablename__ = 'foods_prompted_images'
    id                  = Column(BIGINT, primary_key=True,autoincrement = True)
    food_id             = Column(BIGINT,   nullable=False)
    country_code        = Column(String,          nullable=True)
    store_name          = Column(String,          nullable=True)
    product_name        = Column(String,          nullable=True)
    path                = Column(String,          nullable=True)
    accuracy            = Column(Float,          nullable=True)

    clip                = Column(ARRAY(REAL),          nullable=False)

# Cell
class Indexed (LocalBase):
    __tablename__ = 'indexed'
    id                   = Column(BIGINT,  primary_key=True)
    indexed              = Column(Boolean, nullable   =False)