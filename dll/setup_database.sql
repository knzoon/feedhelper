create table external_feed_read (
	id int(11) not null,
	last_time datetime(6) not null,
	last_zone_id bigint(20) not null,
	last_highest_order bigint(20) not null,
	primary key (id)
);

insert into external_feed_read (id, last_time, last_zone_id, last_highest_order) 
	values (1, utc_timestamp(), 430365, 4000000000);

-- select * from external_feed_read efr;

create table improved_feed_item (
	id UUID not null,
	order_number bigint(20) not null,
	takeover_time datetime(6) not null,
	original_takeover JSON not null,
	primary key (id)
);

create index index_feed_order on improved_feed_item (order_number);

-- select * from improved_feed_item ifi  order by ifi.order_number;  

-- SELECT count(1) from improved_feed_item ifi;