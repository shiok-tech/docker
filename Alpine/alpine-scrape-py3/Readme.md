This docker include all web scrape library, it based on alpine-py3.

1. **Build**

    1.1 Simple
    
        docker build -t alpine-scrape-py3 .
    
    1.2 With alpine version
    
        docker build --build-arg ALPINE_PY3_VERSION=3.11.3 -t alpine-scrape-py3:3.11.3 .

2. **Run**

    2.1 sh
    
        docker run -it --rm alpine-scrape-py3:3.11.3 /bin/ash
     
    2.2 python shell
    
        docker run -it --rm alpine-scrape-py3:3.11.3 python
        Python 3.8.2 (default, Feb 29 2020, 17:03:31)
        [GCC 9.2.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
    
    2.3 call python script
    
        docker run -it --rm -v "$PWD":/scripts alpine-scrape-py3:3.11.3 /bin/ash    
 
 3. **Security**

Suggest add **-u uid:pid** to let docker run at non-root account, otherwise all contents generate will belong to root.

For example:

    ```
    docker run -u 1000:1000 -it --rm -v "$PWD":/test alpine-scrape-py3
    cd /test
    touch a
    exit
    ```
    
You will find the file "a" belong to 1000:1000

