create table bds35_tbl1 (
student_id int,
stud_fname varchar(255),
stud_mname varchar(255),
stud_lname varchar(255),
stud_age int);


insert into bds35_tbl1 (student_id, stud_fname, stud_mname, stud_lname, stud_age) values (17, 'Anurag','Arun','Edlabadkar',46);
insert into bds35_tbl1 values (12, 'Manisha', 'Maya', 'Poudel',27);
insert into bds35_tbl1 values (13, 'Emma','Bale','Smith',28);
insert into bds35_tbl1 values (18, 'Ananya','Pradhan','Mishra',16); 

select * from bds35_tbl1;
 
/*
NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
CREATE INDEX - Used to create and retrieve data from the database very quickly
 
--Table A - student_id Primary
--Table B - student_year_enroll Primary student_id Secondary/Foreign
--Table C - student_sub_enroll Primary student_id, student_year_enroll Secondary/Foreign
*/

create table bds35_nn(
id int not null,
fname varchar(255) not null,
lname varchar(255) not null);

insert into bds35_nn values (1191, 'Pritam', 'Shah');
insert into bds35_nn values (1192, 'Ramana', 'Verma');
insert into bds35_nn values (1194, 'Mani' , 'Patel'); 

create table bds35_unq(
id int not null,
fname varchar(255) not null,
lname varchar(255) not null,
unique (id));

 

create table bds35_prim(
id int not null,
fname varchar(255) not null,
lname varchar(255) not null,
primary key (id));

drop table bds35_prim;

insert into bds35_prim values (1234, 'Viju', 'Shah');
insert into bds35_prim values (1235, 'Vijay', 'Shah');
insert into bds35_prim values (1236, 'Vijayan', 'Shah');
insert into bds35_prim values (1237, 'Vijayta', 'Shah');
insert into bds35_prim values (1238, 'Vijan', 'Shah');

create table bds35_fore(
order_id int not null,
order_number int not null,
ID int,
PRIMARY KEY (order_id),
CONSTRAINT FK_id FOREIGN KEY (ID)
REFERENCES bds35_prim(ID)
);

drop table bds35_fore;

insert into bds35_fore values (7651234, 98765, 1234);
insert into bds35_fore values (7651235, 98765, 1234);
insert into bds35_fore values (7651236, 98765, 1234);
insert into bds35_fore values (7651237, 98765, 1234);
insert into bds35_fore values (7651238, 98765, 1234);

insert into bds35_fore values (7651239, 98766, 1235);
insert into bds35_fore values (7651240, 98766, 1235);
insert into bds35_fore values (7651241, 98766, 1235);
insert into bds35_fore values (7651242, 98766, 1235);
insert into bds35_fore values (7651243, 98766, 1235);


insert into bds35_fore values (7651244, 98767, 1236);
insert into bds35_fore values (7651245, 98767, 1236);
insert into bds35_fore values (7651246, 98767, 1236);
insert into bds35_fore values (7651247, 98767, 1236);
insert into bds35_fore values (7651248, 98767, 1236);


insert into bds35_fore values (7651249, 98768, 1237);
insert into bds35_fore values (7651250, 98768, 1237);
insert into bds35_fore values (7651251, 98768, 1237);
insert into bds35_fore values (7651252, 98768, 1237);
insert into bds35_fore values (7651253, 98768, 1237);

 
insert into bds35_fore values (7651254, 98769, 1238);
insert into bds35_fore values (7651255, 98769, 1238);
insert into bds35_fore values (7651256, 98769, 1238);
insert into bds35_fore values (7651257, 98769, 1238);
insert into bds35_fore values (7651258, 98769, 1238);

 
select * from bds35_fore;


select * from bds35_nn;

 
select * from bds35_nn
where
fname = 'Pritam';

 
select * from bds35_nn
where 
id = 1192;

 

select * from bds35_nn
where
fname = 'Pritam' and id=1192;

select * from bds35_nn
where
fname = 'Pritam' or id=1192;

 
select * 
from 
bds35_prim a,
bds35_fore b
where 
a.id = b.id and 
a.fname = 'Vijay' and 
a.lname = 'Shah';

select * 
from 
bds35_prim x,
bds35_fore y
where
x.id = y.id and
y.order_id between 7651238 and 7651258 and
y.order_number between 98765 and 98768;


select * from bds35_nn;

SET SQL_SAFE_UPDATES = 0;
update bds35_nn
set fname = 'HariOm'
WHERE id = 1191;

select * from bds35_nn;

set SQL_SAFE_UPDATES = 0;
update bds35_nn
set id = 1198
WHERE id = 1191;

select * from bds35_nn;

select * from bds35_prim;

update bds35_prim
set id = 1995
where id = 1234;

select * from bds35_nn;

set SQL_SAFE_UPDATES = 0;
update bds35_nn
set fname = 'Krishna'
where id = 1192;

select * from bds35_nn;

select * from bds35_fore;

select * from bds35_fore
where order_id = 7651234;

delete from bds35_fore
where id = 1234;

select * from bds35_fore
where order_id = 7651234;










