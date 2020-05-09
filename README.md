# Building
docker build -t ds_day_in_the_life:0.0.1 . 

# Running
docker run -it --rm -p 8888:8888 ds_day_in_the_life:0.0.1

Then point a browser at <IP of docker host>:8888
