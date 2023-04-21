STUDENTS:
  CELINE ODDING
  MARGARIDA GONÇALVES


The app connects to mongoDB, and it inserts documents into the existing collection. We have tested it several times, and each time the code is executed (or the docker image is run) it adds 100 more documents into the collection called city_weather.

In the .zip file, we also have a .txt file with the credentials to access the cluster in mongoDB. 
We built the image, ran it to see if it was working properly, and then created the docker-compose file, which also runs everything correctly.

Each time the docker container is run, all the documents in the collection and the number of documents will be printed.
 
With each run, we get to see the number of documents in the collection increasing. 
We tagged and pushed the image into the docker hub successfully.


The image can be pulled in https://hub.docker.com/r/margaridaslima/weather_collection
and run using docker run margaridaslima/weather_collection


