This docker can be used as a basic alpine image, it include timezone setting.

1. **Build**

    1.1 Simple
    
        docker build -t alpine-timezone .
    
    1.2 With alpine version
    
        docker build --build-arg ALPINE_VERSION=3.11.3 -t alpine-timezone:3.11.3 .
    
    1.3 With alpine version and timezone
    
        docker build \
           --build-arg ALPINE_VERSION=3.11.3 \
           --build-arg TIMEZONE="Asia/Singapore" \
           -t alpine-timezone:3.11.3 .

2. **Run**

    ```
	docker run -it --rm alpine-timezone:3.11.3
    ```
   
3. **Security**

Suggest add **-u uid:pid** to let docker run at non-root account, otherwise all contents generate will belong to root.

For example:

    docker run -u 1000:1000 -it --rm -v "$PWD":/test alpine-timezone
    cd /test
    touch a
    exit

You will find the file "a" belong to 1000:1000

