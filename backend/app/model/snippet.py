# In der Datei: backend/app/model/code_snippet.py

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CodeSnippet(Base):
    __tablename__ = 'code_snippets'
    # ID
    name = Column(String(255), primary_key=True)
    code = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

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
