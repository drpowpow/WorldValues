from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3
import pdb
from mysolr import Solr
import requests
from contextlib import closing
from flask.ext.sqlalchemy import SQLAlchemy

#configuration must have the full path
DATABASE = 'c:/Users/Alicia/PycharmProjects/WorldValues/worldvalues.db'
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD = 'default'
solr = Solr('http://localhost:8983/solr/#/collection1')


app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    cur= g.db.execute('select * from questionsonly where show=1 order by QuestOrder desc')
    questions = [dict(questionnum=row[0],question=row[1],answer1=row[2], answer2=row[3], answer3=row[4],answer4=row[5],answer5=row[6],answer6=row[7],answer7=row[8],answer8=row[9],answer9=row[10],answer10=row[11]) for row in cur.fetchall()]
    return render_template('show_questions.html', questions=questions)
#todo: variable number of answers using-twitter-bootstrap-radio-buttons-with-Flask stackoverflow
#todo: validate forms

@app.route('/add',  methods=['GET', 'POST'])
def add_entry():
    #if not session.get('logged_in'):
    #    abort(401)
    #todo: query solr
    #request.form is an immtauble multi dictionary
    #imd=request.form;imd.to_dict();iterate over dictionary for key,value in d.iteritems():;get keys d.keys() or values d.values()
    if request.method == "POST":
        #post to database
        imd = request.form.to_dict()
        keys = imd.keys()
        values = imd.values()
        listofanswers = str(keys)[1:-1]
        quest="?," * (len(keys)-1)+"?"
        sqlcommand="insert into newresponse ("+listofanswers+") values("+quest+")"
        g.db.execute(sqlcommand,values)
        g.db.commit()
        documents=lookup(imd)
        flash('New entry was successfully posted')
        #query solr
        # -4:Not asked, -3:Not Applicable, -2:No Answer, -1: Don't know
    return render_template('search.html',documents=documents)

def lookup(imd):
        curquest= g.db.execute('select QuestionID from questionsonly where show=1 order by QuestOrder desc')
        allquestions=[]
        query=""
        for row in curquest.fetchall():
            allquestions.append(row[0])
        #pdb.set_trace()
        for quest in allquestions:
            if quest in imd.keys():
                i=imd.keys().index(quest)
                query=query+'+'+str(quest)+":"+str(imd.values()[i])+" "
            #else:
                #query=query+" +"+str(quest)+":"+'"-2"'

        response = solr.search(q=query,rows=10, start=0)
        #response = solr.search(q='+V2:12 +V5:3',rows=10, start=0)
        documents = response.documents
        #pdb.set_trace()
        return documents;
        #solrquery=

#todo: add translation with jinja and babel
#todo: refactor with create query as its own thing

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/search')
def findanswer():
    return

if __name__ == '__main__':
    app.debug=True
    app.run()
