import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'Publisher: {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id', ondelete='CASCADE'), nullable=False)

    publisher = relationship('Publisher', backref='book')

    def __str__(self):
        return f'Book:{self.id} | {self.title}'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60))

    def __str__(self):
        return f'Shop: {self.name}'

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id', ondelete='CASCADE'), nullable=False,)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id', ondelete='CASCADE'), nullable=False,)
    count = sq.Column(sq.Integer)

    book = relationship('Book', backref='stock')
    shop = relationship('Shop', backref='stock')
    sale = relationship('Sale', backref='stock')

    def __str__(self):
        return f'Stock: {self.count}'

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.DATE)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id', ondelete='CASCADE'), nullable=False,)
    count = sq.Column(sq.Integer)

    def __str__(self):
        return f'Sale: {self.price} | {self.date_sale} | {self.count}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)