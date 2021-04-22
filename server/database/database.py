import datetime

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Ipids(Base):
    __tablename__ = 'ipids'

    ipid = Column(Integer, primary_key=True)
    ip_address = Column(String, nullable=False)

class Misc_Event_Types(Base):
     __tablename__ = 'misc_event_types'

     type_id = Column(Integer, primary_key=True)
     type_name = Column(String)
     
     def __repr__(self):
         return "<Misc_Event_Types(type_id='%s', type_name='%s')>" % (self.type_id, self.type_name)

class Misc_Events(Base):
    # PRIMARY KEY HERE IS NOT REAL
    __tablename__ = 'misc_events'

    event_time = Column(DateTime, default=datetime.datetime.utcnow, primary_key=True)
    ipid = Column(
        Integer,
        ForeignKey('ipids.ipid', ondelete='CASCADE')
        )
    target_ipid = Column(
        Integer,
        ForeignKey('ipids.ipid', ondelete='CASCADE')
        )
    event_subtype = Column(
        Integer,
        ForeignKey('misc_event_types.type_id'),
        nullable=False)
    event_data = Column(String)

class Ip_Bans(Base):
    __tablename__ = 'ip_bans'

    ipid = Column(Integer, primary_key=True)
    ban_id = Column(Integer, nullable=False)

class Hdid_Bans(Base):
    __tablename__ = 'hdid_bans'

    hdid = Column(String, primary_key=True)
    ban_id = Column(Integer)

class Connect_Events(Base):
    __tablename__ = 'connect_events'

    event_time = Column(DateTime, primary_key=True, default=datetime.datetime.now())
    ipid = Column(Integer, ForeignKey('ipids.ipid'), nullable=False)
    hdid = Column(String, nullable=False)
    failed = Column(Integer, default=0)



class Hdids(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'hdids'

    hdid = Column(String, primary_key=True)
    ipid = Column(
        Integer,
        ForeignKey('ipids.ipid'),
        nullable=False
        )

class IC_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'ic_events'

    event_time = Column(DateTime, primary_key=True, default=datetime.datetime.now())
    ipid = Column(Integer, ForeignKey('ipids.ipid'), nullable=False)
    room_name = Column(String)
    ic_name = Column(String)
    message = Column(String, nullable=False)

class Area(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'area'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Login_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'login_events'

    event_time = Column(DateTime, primary_key=True, default=datetime.datetime.now())
    ipid = Column(Integer, ForeignKey('ipids.ipid'), nullable=False)
    profile_name = Column(String)

class Room_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'room_events'

    # event_id = Column(Integer)
    event_time = Column(DateTime, primary_key=True, default=datetime.datetime.now())
    ipid = Column(Integer, ForeignKey('ipids.ipid'), nullable=False)
    target_ipid = Column(Integer)
    room_name = Column(String)
    char_name = Column(String)
    ooc_name = Column(String)
    event_subtype = Column(Integer, ForeignKey('room_event_types.type_id'), nullable=False)
    message = Column(String)

class Room_Event_Types(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'room_event_types'

    type_id = Column(Integer, primary_key=True)
    type_name = Column(String, nullable=False)

class Bans(Base):
    # FILL ME OUT PROPERLY
     __tablename__ = 'bans'

     ban_id = Column(Integer, primary_key=True)
     ban_date = Column(DateTime, default=datetime.datetime.now())
     unban_date = Column(DateTime)
     banned_by = Column(Integer)
     reason = Column(String)

Base.metadata.create_all(engine)

ed_user = Misc_Event_Types(type_id=0, type_name='Testing')
session.add(ed_user)
our_user = session.query(Misc_Event_Types).filter_by(type_name='Testing').first() 
print(our_user)
