import sqlalchemy

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/crud'

# Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
print(engine.table_names())
