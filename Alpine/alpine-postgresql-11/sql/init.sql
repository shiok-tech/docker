CREATE TABLE LOCUS  (
    "TIMESTAMP"                 timestamp NOT NULL,
    "USERID"               varchar(32) NOT NULL,
    "CGI"                   varchar(20) NULL,
    "LATITUDE"             float NULL,
    "LONGITUDE"            float NULL,
    "MCC"                  int NULL,
    "MNC"                  varchar(3) NULL,
    "TRAFFIC"              int NULL,
    "SITE_TYPE"        int NULL
);
CREATE INDEX idx_time ON LOCUS("TIMESTAMP");
