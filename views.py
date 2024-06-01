from flask import Blueprint, render_template, request, redirect, url_for
from .models import Product
from .database import SQLAlchemySingleton
import json
from .serializer import serialize_model_instance

db = SQLAlchemySingleton.get_instance()

main = Blueprint('main',__name__)
products_bp = Blueprint('products', __name__, url_prefix='/products')

@main.route('/')
def index():
    return render_template('index.html')

@products_bp.route('/')
def list_products():
    products = Product.query.all()
    cleaned_dict = {}
    for product in products:
        cleaned_product= serialize_model_instance(product)
        cleaned_dict[cleaned_product['code']] = cleaned_product
    return json.dumps(cleaned_dict)

@products_bp.route('/create', methods=['GET', 'POST'])
def create_product():
    code = request.form['code'] 
    description = request.form['description']
    status = request.form['status']
    expireDate = request.form['expireDate']
    product = Product(code=code, description=description, status=status, expireDate=expireDate)        
    db.session.add(product)
    db.session.commit()        
    cleaned_product = serialize_model_instance(product)
    return cleaned_product

@products_bp.route('/<code>')
def view_product(code):
    product = Product.query.filter_by(code=code).first_or_404()
    cleaned_product = serialize_model_instance(product)
    return cleaned_product

@products_bp.route('/<code>/update', methods=['GET', 'POST'])
def update_product(code):
    product = Product.query.filter_by(code=code).first_or_404()
    product.description = request.form['description']
    product.status = request.form['status']

    product.expireDate = request.form['expireDate']
    db.session.commit()
    cleaned_product = serialize_model_instance(product)
    return cleaned_product

@products_bp.route('/<code>/delete', methods=['POST'])
def delete_product(code):
    product = Product.query.filter_by(code=code).first_or_404()
    db.session.delete(product)
    db.session.commit()
    cleaned_product = serialize_model_instance(product)
    return cleaned_product
