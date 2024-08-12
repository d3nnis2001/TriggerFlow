-- codesnippets for the editor
CREATE TABLE codesnippets ( id interger primary key, name text not null, code text not null, date date not null);


-- table for user
CREATE TABLE user ( id integer primary key, first_name text not null, last_name text not null, email text not null, password text not null, role text not null, firma text not null)

-- Insert query for inserting a new user
insert into user (id, first_name, last_name, email, password, role, firma) VALUES (1, 'Dennis', 'Schielke', 'd3nnis.s@web.de', 'admin123', 'admin', 'TriggerYou GmbH');
