1. Build
```
docker build -t alpine-grafana-7-1-1 .
```

2. Run
```
docker run -d -p 3000:3000 --name grafana alpine-grafana-7-1-1
```