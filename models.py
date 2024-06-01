from sqlalchemy.dialects.postgresql import ENUM
from .database import SQLAlchemySingleton

db = SQLAlchemySingleton.get_instance()

status_enum = ENUM('Active', 'Inactive', name='status_enum')

class Product(db.Model):
    __tablename__ = 'productos'
    code = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(status_enum, nullable=False)
    expireDate = db.Column(db.Date)

    def __repr__(self):
        return f"<Product {self.code}: {self.description}>"
