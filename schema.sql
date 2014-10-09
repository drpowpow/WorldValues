drop table if exists entries;
create table entries (
   id integer primary key autoincrement,
   title text not null,
   text text not null
);


/* create table question (question_id text, question_name text, answer_1 text, answer_2 text, answer_3 text, answe
r_4 text);
create table country (country_id integer, country_name text, in_analysis integer)
create table answer (country_id integer, person_id integer, V4 integer, V5 integer, V6 integer, V7 integer, V8
integer, V9 integer)

curl http://localhost:8983/solr/update/csv --data-binary @books.csv -H 'Content-type:text/plain; charset=utf-8'
*/

