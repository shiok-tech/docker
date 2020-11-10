1. **Build**

   ```
   1. docker build -t alpine-postgre-12 .
   2. docker build --build-arg ALPINE_TZ_VERSION=3.12.1 -t alpine-postgre-12:3.12.1 .
   ```

2. **Run**

   ```
   docker run --name postgre_db -d -e POSTGRES_PASSWORD=1234567 -v "$PWD/data":/var/lib/postgresql/data -p 5432:5432 alpine-postgre-11
   ```

   > create data folder under running directory, postgres will create database files at this folder

   > For windows, need create a share volumn first, then use this as volumn to mapping

   ```
   docker volume create --name postgre_data -d local
   docker run --name postgre_db -d -e POSTGRES_PASSWORD=1234567 -v postgre_data:/var/lib/postgresql/data -p 5432:5432 alpine-postgre-11
   ```

   > validate

   ```
   docker exec -it postgre_db /bin/sh
   su - postgres
   psql -U postgres -d postgres -h 127.0.0.1 -p 5432
   select version();
   ```
