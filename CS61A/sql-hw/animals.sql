create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;

select max(legs) from animals;

select sum(weight) from animals;

select max(weight), kind from animals group by legs having count(*) > 1;

select count(*) from animals;

create table diff as
  select a.legs - b.legs, a.kind, b.kind from animals as a, animals as b where a.weight=b.weight and
         a.kind <> b.kind;

select max(a.legs-b.legs) from animals as a,animals as b where a.weight = b.weight;

select max(legs) - min(legs) as diff from animals group by weight order by -diff limit 1;
