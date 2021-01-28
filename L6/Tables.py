from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
PATH_DB = 'ProjectDB.sqlite3'
engine = create_engine(f'sqlite:///{PATH_DB}?check_same_thread=False')


class Categories(base):
    __tablename__ = 'categories'
    category = Column(Integer, primary_key=True)
    category_name = Column(String(100), nullable=False)
    category_description = Column(String(300), nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    def __repr__(self):
        return "<Categories(category_name='%s')>" % self.category_name


class Units(base):
    __tablename__ = 'units'
    unit = Column(String(20), primary_key=True, nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return "<Units(unit='%s')>" % self.unit


class Positions(base):
    __tablename__ = 'positions'
    position = Column(String(100), primary_key=True, nullable=False)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return "<Positions(position='%s')>" % self.position


class Goods(base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(100))
    good_unit = Column(Integer, ForeignKey('units.unit'))
    good_cat = Column(Integer, ForeignKey('categories.category'))

    def __init__(self, good_name, good_unit, good_cat):
        self.good_name = good_name
        self.good_unit = good_unit
        self.good_cat = good_cat

    def __repr__(self):
        return "<Goods(good_name='%s', good_unit='%s', good_cat='%s')>" % (self.good_name,
                                                                           self.good_unit,
                                                                           self.good_cat)


class Employees(base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(100))
    employee_position = Column(String(100), ForeignKey('positions.position'))

    def __init__(self, employee_fio, employee_position):
        self.employee_fio = employee_fio
        self.employee_position = employee_position

    def __repr__(self):
        return "<Employees(employee_fio='%s', employee_position='%s')>" % (self.employee_fio,
                                                                           self.employee_position)


class Vendors(base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(300))
    vendor_ownerchipform = Column(String(100))
    vendor_address = Column(String(200))
    vendor_phone = Column(String(50))
    vendor_email = Column(String(50))

    def __init__(self, vendor_name, vendor_ownerchipform, vendor_address, vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_ownerchipform = vendor_ownerchipform
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return "<Vendors(vendor_name='%s', vendor_ownerchipform='%s', vendor_address='%s', vendor_phone='%s', " \
               "vendor_email='%s')>" % (self.vendor_name,
                                        self.vendor_ownerchipform,
                                        self.vendor_address,
                                        self.vendor_phone,
                                        self.vendor_email)


base.metadata.create_all(engine)
vendor = Vendors('News company', 'АО', 'Lenin str. 20', '+7555 111 222', 'newscompany@email.com')
session = sessionmaker(bind=engine)
session_ob = session()
session_ob.add(vendor)
session_ob.commit()
