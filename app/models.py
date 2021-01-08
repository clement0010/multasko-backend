from app import db
import datetime

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.datetime.now)
    priority_level = db.Column(db.Integer, default=0)
    text_type = db.Column(db.Integer, default=0)
    summary = db.Column(db.String, nullable=True)
    category_id = db.Column(db.String, db.ForeignKey('category.id'), nullable=True)


    def __repr__(self):
        return '<Memo {}>'.format(self.text)    

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id' : self.id,
           'text' : self.text,
           'priority_level' : self.priority_level,
           'text_type': self.text_type,
           'summary': self.summary,
           'category_id': self.category_id,
           'date_posted': dump_datetime(self.date_posted),

       }
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    memos = db.relationship('Memo',backref='category',lazy=True)

    def __repr__(self):
        return '<Category {}>'.format(self.name)    
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id' : self.id,
           'name' : self.name,
            'memos' :[memo.serialize for memo in self.memos]
       }