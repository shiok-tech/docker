#!/bin/bash    
docker run \
    --name postgre_db -d \
    -e POSTGRES_PASSWORD=parquet \
    -v "$PWD/data":/var/lib/postgresql/data \
    -v "$PWD/sql":/home/sql \
    -p 5432:5432 \
    alpine-postgresql-12:3.12.1
