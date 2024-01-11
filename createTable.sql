CREATE TABLE IF NOT EXISTS parkrecords(
   City     VARCHAR(16) NOT NULL
  ,Plate    VARCHAR(7) NOT NULL
  ,Name     VARCHAR(18) NOT NULL
  ,Make     VARCHAR(5) NOT NULL
  ,Model    VARCHAR(3) NOT NULL
  ,Category VARCHAR(5) NOT NULL
  ,Year     INTEGER  NOT NULL
  ,ID       VARCHAR(36) NOT NULL PRIMARY KEY
  ,TS       timestamp without time zone NOT NULL
  ,Price	float 
);