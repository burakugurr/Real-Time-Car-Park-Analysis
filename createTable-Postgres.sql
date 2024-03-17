CREATE TABLE IF NOT EXISTS parkrecords(
  city     VARCHAR(16) NOT NULL
  ,plate    VARCHAR(7) NOT NULL
  ,name     VARCHAR(18) NOT NULL
  ,make     VARCHAR(5) NOT NULL
  ,model    VARCHAR(3) NOT NULL
  ,category VARCHAR(5) NOT NULL
  ,year     INTEGER  NOT NULL
  ,id       VARCHAR(36) NOT NULL PRIMARY KEY
  ,ts       timestamp without time zone NOT NULL
  ,exit_TS	timestamp without time zone
  ,price float
);