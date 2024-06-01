from flask_sqlalchemy import SQLAlchemy

class SQLAlchemySingleton:
    _instance = None

    @staticmethod
    def get_instance(app=None):
        if SQLAlchemySingleton._instance is None:
            SQLAlchemySingleton._instance = SQLAlchemy(app)
        elif app is not None:
            SQLAlchemySingleton._instance.init_app(app)
        return SQLAlchemySingleton._instance
