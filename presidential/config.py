
SQLALCHEMY_DATABASE_URI  = 'mysql+pymysql://root:root@localhost/PRESIDENTIAL'

#######
# testing the url works
#from sqlalchemy import create_engine
#engine = create_engine('mysql+pymysql://root:root@localhost/PRESIDENTIAL')
#from sqlalchemy import inspect
#inspector = inspect(engine)

#for table_name in inspector.get_table_names():
#   for column in inspector.get_columns(table_name):
#       print("Column: %s" % column['name'])
