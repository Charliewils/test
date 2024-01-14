create table ints as
  select "zero" as word, 0 as one, 1 as two, 2 as three union
  select "one"	       , 1       , 2       , 3          union
  select "three"       , 4       , 5       , 6          union
  select "four"        , 7       , 8       , 9;
