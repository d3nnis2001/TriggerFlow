from datetime import datetime
from app import db

class CodeSnippet(db.Model):
    __tablename__ = 'code_snippets'
    name = db.Column(db.String(255), primary_key=True)
    code = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"<CodeSnippet(name='{self.name}', created_at='{self.created_at}')>"

    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'created_at': self.created_at.isoformat()
        }
