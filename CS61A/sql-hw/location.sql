CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42,              71,              "Cambridge"        UNION
  SELECT 45,              93,              "Minneapolis"      UNION
  SELECT 33,             117,              "San Diego"        UNION
  SELECT 26,              80,              "Miami"            UNION
  SELECT 90,               0,              "North Pole";

create table cold as
  select name from cities where latitude > 43 union
  select "Chicago";

select name, "is cold" from cold;

create table distances as
  select a.name as first, b.name as second,
	 60*(a.latitude - b.latitude) as distance
	 from cities as a, cities as b
	 where a.name != b.name
	 order by a.longitude;
