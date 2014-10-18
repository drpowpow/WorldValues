drop table if exists entries;
create table entries (
   id integer primary key autoincrement,
   title text not null,
   text text not null
);
drop table if exists countriesonly;
create table countriesonly(
  CountryID text primary key,
  CountryName text not null,
  InAnalysis integer
);
drop table if exists answersonly;
create table answersonly(
ID integer,
V2 integer,
V3 integer,
V4 integer,
V5 integer,
V6 integer,
V7 INTEGER,
V8 integer,
V9 integer,
V12 integer,
V13 integer,
V14 integer,
V15 integer,
V16 integer,
V17 integer,
V18 integer,
V19 integer,
V20 integer,
V21 integer,
V22 integer,
V23 integer,
V242 integer,
V238 integer,
V240 integer,
V245 integer,
V248 integer,
V250 integer,
V255 integer
);
drop table if exists questionsonly;
create table questionsonly(
 QuestionID text primary key,
 QuestionText text not null,
 Answer1 text,
 Answer2 text,
 Answer3 text,
 Answer4 text,
 Answer5 text,
 Answer6 text,
 Answer7 text,
 Answer8 text,
 Answer9 text,
 Answer10 text,
 Show int,
 QuestOrder int
);
drop table if exist newresponse;
create table newresponse(
 UserID text primary key autoincrement,
 V2 integer,
V3 integer,
V4 integer,
V5 integer,
V6 integer,
V7 INTEGER,
V8 integer,
V9 integer,
V12 integer,
V13 integer,
V14 integer,
V15 integer,
V16 integer,
V17 integer,
V18 integer,
V19 integer,
V20 integer,
V21 integer,
V22 integer,
V23 integer,
V242 integer,
V238 integer,
V240 integer,
V245 integer,
V248 integer,
V250 integer,
V255 integer,
Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
