from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

app = Flask(__name__)

ENV = 'dev'
   
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:S9emub7v@localhost/teacher'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xkbosnnjreognb:9a4eac938ed3590f1931315bd185efa3f8d98ce6c6ace26160c298402ae19be8@ec2-54-235-104-136.compute-1.amazonaws.com:5432/dckefpmha2quh8'

app.config['SQLALCHEMY_TRACK_MODICATIONS'] = False

#Init db
db = SQLAlchemy(app)

#Adding Migrator
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#Init ma
ma = Marshmallow(app)

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    library = db.Column(db.String(200))
    reviewed = db.Column(db.Boolean)
    visibility = db.Column(db.String(200))
    type = db.Column(db.String(200))
    qtext = db.Column(db.Text())

    def __init__(self, title, library, reviewed, visibility, type, qtext):
        self.title = title
        self.library = library
        self.reviewed = reviewed
        self.visibility = visibility
        self.type = type
        self.qtext = qtext

#Question Schema
class QuestionSchema(ma.Schema):
    class Meta:
        fields = ('id','title','library','reviewed','visibility','type', 'qtext')

#Init Schema
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)


#Get All Question
@app.route('/get-question', methods=['GET'])
#design pattern in Python that allows a user to add 
#new functionality to an existing object without modifying its structure.
def get_questions():
    all_questions = Questions.query.all()
    result = questions_schema.dump(all_questions)
    return jsonify(result)

#Get Single question
@app.route('/get-question/<id>', methods=['GET'])
#design pattern in Python that allows a user to add 
#new functionality to an existing object without modifying its structure.
def get_single_question(id):
    question = Questions.query.get(id)
    return question_schema.jsonify(question)

#@app.route("/") is a decorator which adds an endpoint to the app object. 
#It doesn't actually modify any behavior of the function, and is instead sugar to simplify the process.
@app.route('/question', methods=['POST'])
def add_question():
    if request.method == 'POST':
        title = request.json['title']
        library = request.json['library']
        reviewed = request.json['reviewed']
        visibility = request.json['visibility']
        type = request.json['type']
        qtext = request.json['qtext']

        print(title, library, reviewed, visibility, type, qtext)
        question = Questions(title, library, reviewed, visibility, type, qtext)
        db.session.add(data)
        db.session.commit()
        return question_schema.jsonify(question)

#Update a Question
@app.route('/question/<id>', methods=['PUT'])
def update_question(id):
    if request.method == 'PUT':
        question = Questions.query.get(id)
        title = request.json['title']
        library = request.json['library']
        reviewed = request.json['reviewed']
        visibility = request.json['visibility']
        type = request.json['type']
        qtext = request.json['qtext']

        print(title, library, reviewed, visibility, type, qtext)

        question.title = title
        question.library = library
        question.reviewed = reviewed
        question.visibility = visibility
        question.type = type
        question.qtext = qtext 

        db.session.commit()

        return question_schema.jsonify(question)

#Delete Single question
@app.route('/delete-question/<id>', methods=['DELETE'])
#design pattern in Python that allows a user to add 
#new functionality to an existing object without modifying its structure.
def delete_question(id):
    question = Questions.query.get(id)
    db.session.delete(question)
    db.session.commit()
    return 'deleted'


if __name__ == '__main__': 
    app.run()