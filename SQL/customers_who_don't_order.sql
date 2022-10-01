/*

Create table If Not Exists Customers (id int, name varchar(255))
Create table If Not Exists Orders (id int, customerId int)
Truncate table Customers
insert into Customers (id, name) values ('1', 'Joe')
insert into Customers (id, name) values ('2', 'Henry')
insert into Customers (id, name) values ('3', 'Sam')
insert into Customers (id, name) values ('4', 'Max')
Truncate table Orders
insert into Orders (id, customerId) values ('1', '3')
insert into Orders (id, customerId) values ('2', '1')


Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key column for this table.
customerId is a foreign key of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

*/

Create table Customers
(
    id int,
    name varchar(255)
)
Create table Orders
(
    id int,
    customerId int
)
Truncate table Customers
insert into Customers
    (id, name)
values
    ('1', 'Joe')
insert into Customers
    (id, name)
values
    ('2', 'Henry')
insert into Customers
    (id, name)
values
    ('3', 'Sam')
insert into Customers
    (id, name)
values
    ('4', 'Max')
Truncate table Orders
insert into Orders
    (id, customerId)
values
    ('1', '3')
insert into Orders
    (id, customerId)
values
    ('2', '1')


select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid
from orders
);