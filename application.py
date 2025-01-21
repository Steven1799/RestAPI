from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Actions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"
@app.route('/')
def index():
    return 'Hello World 2!'

@app.route('/journal')
def get_actions():
    actions = Actions.query.all()
    output = []
    for action in actions:
        action_data = {'name':action.name,'description':action.
                      description}
        output.append(action_data)
    return {"actions":output}

@app.route('/journal/<id>')
def get_action(id):
    action = Actions.query.get_or_404(id)
    return {"name":action.name,"description":action.description} # use jsonify if not dealing with dict

@app.route('/journal',methods=['POST'])
def add_action():
    action = Actions(name=request.json['name'],
                     description=request.json['description'])
    db.session.add(action)
    db.session.commit()
    return {'id':action.id}

@app.route('/journal/<id>',methods=['DELETE'])
def delete_drink(id):
    action = Actions.query.get(id)
    if action is None:
        return {"Message":"404"}
    db.session.delete(action)
    db.session.commit()
    return {'Message':"Deleted!"}