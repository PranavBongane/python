from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from db_config import SessionLocal, engine
import db_model
from sqlalchemy.orm import Session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
db_model.Base.metadata.create_all(bind= engine)

def init_db():
    db = SessionLocal()
    count = db.query(db_model.Product).count()
    if count == 0:
        products = [
            Product(id= 1, name= "phone", description= "budget phone", price= 99, quantity= 10),
            Product(id= 2, name= "laptop", description= "gaming laptop", price= 999, quantity= 99),
            Product(id= 3, name= "pen", description= "writing instrument", price= 9, quantity= 72),
            Product(id= 4, name= "stand", description= "phone stand", price= 50, quantity= 67),
            Product(id= 5, name= "bottle", description= "water bottle", price= 94, quantity= 56),
            Product(id= 6, name= "speaker", description= "bluetooth speaker", price= 85, quantity= 15)
        ]
        for product in products:
            db.add(db_model.Product(**product.dict()))
        db.commit()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

init_db()

@app.get("/")
def greet():
    return "WELCOME to prana!"

@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    db_products = db.query(db_model.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(db_model.Product(**product.dict()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        return "product updated successfully"
    return {"error": "Product not found"}

@app.delete("/products/{id}")    
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
    return {"error": "Product not found"}  

