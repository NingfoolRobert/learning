
use mysql;

create database  db_ops default charset utf8mb4 collate utf8_gearnal_ci;

show databases;

use db_ops;

show tables;


create  table tb_depart(
	id 					int 				primary key auto_increment not null, 
	depart_name 		varchar(64) 		not null,
	memo 				varchar(256) 		
)default  charset=utf8;
#用户表
create  table tb_user(
	id 					bigint 				primary key auto_increment  not null, 
	name 				varchar(64) 		not null, 
	email 				varchar(128) 		unique not null, 
	phone 				varchar(11)			, 
	depart_id 			int 				not null,   
	pwd 				varchar(128)		not null, 
	attr 				bigint 				default 0,
	foreign key (depart_id) references tb_depart(id)
)default  charset=utf8mb4;


create  table  tb_file(
	id 					bigint					primary key auto_increment not null,
	app_id 				bigint 					,
	file_name 			varchar(256)			not null,
	md5 				varchar(256)			not null,
	create_time 		DATETIME 				DEFAULT CURRENT_TIMESTAMP, 
	opter_id 			bigint 					not null,
	file_size  			bigint 					not null, 
	file_type 			smallint unsigned  	not null, 
	file_version		int 					not null,
	memo 				varchar(256)		,
	foreign key(opter_id) references tb_user(id)
)default charset=utf8mb4;




create table tb_task(
	id  			bigint 			primary key  auto_increment  not null, 
	task_name 		varchar(128)	not null, 
	create_time 	DATETIME		default current_timestamp,
	schedule_time 	DATETIME		,
	stat 			smallint 		default 0, 
	finsh  			smallint 		default 0,  
	opter_id 		bigint 			not null,
	memo  			varchar(256)	,
	foreign key(opter_id) references tb_user(id)
)default  charset=utf8mb4;

create table tb_task_dtl(
	id 				bigint 			primary key auto_increment not null, 
	task_id 		bigint 			not null,  
	file_id 		bigint 			not null, 
	target_ip 		varchar(16) 	not null,  
	opt 			smallint 		not null,  
	state 			smallint 		not null,  
	create_time 	DATETIME	 	default CURRENT_TIMESTAMP,
	schedule_time 	DATETIME 		,
	finsh_time 		DATETIME 		, 
	memo 			varchar(256) 	,
	foreign key(task_id) references tb_task(id)
)default  charset=utf8mb4;


create  table  tb_app_dep(
	id  			bigint 					primary key auto_increment not null,  
	file_id 		bigint 					not null,
	ip 				varchar(16)				not null, 
	stat 			smallint 				not null default 0,
	dir 			varchar(512)			not null, 
	memo 			varchar(256) 			,
	foreign key(file_id) references tb_file(id)
)default  charset=utf8mb4; 


create table tb_device(
	id 				bigint 					primary key auto_increment not null, 
	ip 				varchar(16)				not null, 
	region 			int 					not null, 
	depart_id 		int 					,
	memo 			varchar(256) 			
)default charset=utf8mb4;


insert  into tb_depart(depart_name)VALUES('行情中心');

select  * from tb_depart ;

select * from  tb_user;


alter table tb_user  
modify email  varchar(128)  not null unique; 

describe  tb_user;

delete  from  tb_user where name='nbf';

set FOREIGN_KEY_CHECKS = 0;
truncate table  tb_user; 
set FOREIGN_KEY_CHECKS=1;

show tables;



drop table  tb_user;
drop table tb_app_info;