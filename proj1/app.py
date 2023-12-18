from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
class User(db.Model):
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    username:Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)