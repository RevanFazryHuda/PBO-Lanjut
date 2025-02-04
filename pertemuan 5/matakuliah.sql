create table matakuliah(
id serial primary key not null,
kodemk varchar(10) unique not null,
namamk varchar(50) not null,
sks enum('1','2','3','4','6') not null);


