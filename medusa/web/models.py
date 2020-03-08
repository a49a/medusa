from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)