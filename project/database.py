from orator import DatabaseManager, Model

DBCONN_ORATOR = {
    'default': 'mysql',
    'mysql' : {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'db_name',
        'user': 'db_user',
        'password': 'db_password',
        'prefix': ''
    }
}

db = DatabaseManager(DBCONN_ORATOR)
Model.set_connection_resolver(db)