from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3 as lite
import csv
import sys
from contextlib import closing
from flask.ext.sqlalchemy import SQLAlchemy
#todo: how to references a folder
#configuration must have the full path
DATABASE = 'c:/Users/Alicia/PycharmProjects/WorldValues/worldvalues.db'
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD = 'default'

app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('startdatabase.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def populate_db():
    db = connect_db()
    cur = db.cursor()
    with open('questionsonly.csv','rb') as fin:
        dr= csv.DictReader(fin)
        to_db=[(i["QuestionID"],i["QuestionText"],i["Answer1"],i["Answer2"],i["Answer3"],i["Answer4"],i["Answer5"],i["Answer6"],i["Answer7"],i["Answer8"],i["Answer9"],i["Answer10"],i["Show"],i["QuestOrder"]) for i in dr]
    cur.executemany("INSERT INTO questionsonly (QuestionID, QuestionText, Answer1, Answer2, Answer3, Answer4, Answer5, Answer6, Answer7, Answer8, Answer9, Answer10,Show, QuestOrder) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
    db.commit()
    with open('answersonly.csv','rb') as fin:
        dr=csv.DictReader(fin)
        to_db=[(i['ID'],i['V2'],i['V3'],i['V4'],i['V5'],i['V6'],i['V7'],i['V8'],i['V9'],i['V12'],i['V13'],i['V14'],i['V15'],i['V16'],i['V17'],i['V18'],i['V19'],i['V20'],i['V21'],i['V22'],i['V23'],i['V242'],i['V238'],i['V240'],i['V245'],i['V248'],i['V250'],i['V255']) for i in dr]
    cur.executemany("INSERT INTO answersonly (ID,V2,V3,V4,V5,V6,V7,V8,V9,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V242,V238,V240,V245,V248,V250, V255) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
    db.commit()
    with open('countriesonly.csv','rb') as fin:
        dr=csv.DictReader(fin)
        to_db=[(i["CountryID"],i["CountryName"],i["InAnalysis"]) for i in dr]
    cur.executemany("INSERT INTO countriesonly (CountryID,CountryName,InAnalysis) VALUES (?,?,?);", to_db)
    db.commit()
    return;

#load data into solr
#curl http://localhost:8983/solr/collection1/update/csv?stream.file=c:/Users/Alicia/PycharmProjects/WorldValues/answersonly.csv

#input data in sqlite3; .header on; .mode csv; .import questionsonly.csv questionsonly
#  .import answersonly.csv answersonly ;import countriesonly.csv countriesonly;
def connect_db():
    return lite.connect(app.config['DATABASE'])
init_db()
populate_db()

