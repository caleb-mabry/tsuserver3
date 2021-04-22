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
    # FILL ME OUT PROPERLY
    __tablename__ = 'ip_bans'

    ipid = Column(Integer)
    ban_id = Column(Integer)

class Hdid_Bans(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'hdid_bans'

    hdid = Column(Integer)
    ban_id = Column(Integer)

class Connect_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'connect_events'

    event_time = Column(Integer)
    ipid = Column(Integer)
    hdid = Column(Integer)
    failed = Column(Integer)



class Hdids(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'hdids'

    hdid = Column(Integer)
    ipid = Column(Integer)

class IC_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'ic_events'

    event_time = Column(Integer)
    ipid = Column(Integer)
    room_name = Column(Integer)
    ic_name = Column(Integer)
    message = Column(Integer)

class Area(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'area'

    id = Column(Integer)
    name = Column(Integer)

class Login_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'login_events'

    event_time = Column(Integer)
    ipid = Column(Integer)
    profile_name = Column(Integer)

class Room_Events(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'room_events'

    event_id = Column(Integer)
    event_time = Column(Integer)
    ipid = Column(Integer)
    target_ipid = Column(Integer)
    room_name = Column(Integer)
    char_name = Column(Integer)
    ooc_name = Column(Integer)
    event_subtype = Column(Integer)
    message = Column(Integer)

class Room_Event_Types(Base):
    # FILL ME OUT PROPERLY
    __tablename__ = 'room_event_types'

    type_id = Column(Integer)
    type_name = Column(Integer)

class Bans(Base):
    # FILL ME OUT PROPERLY
     __tablename__ = 'bans'

     ban_id = Column(Integer, primary_key=True)
     ban_date = Column(DateTime)
     unban_date = Column(DateTime)
     banned_by = Column(Integer)
     reason = Column(String)

Base.metadata.create_all(engine)

ed_user = Misc_Event_Types(type_id=0, type_name='Testing')
session.add(ed_user)
our_user = session.query(Misc_Event_Types).filter_by(type_name='Testing').first() 
print(our_user)
