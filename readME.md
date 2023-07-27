## Benutzung
1. Download Git-Repository (via Zip-File or Git Clone)
2. Install Docker (https://docs.docker.com/engine/install/)
3. Open Terminal in Working Directory yt_schnulzen
4. Create the Docker Image, by executing:
```
$ docker build -t my_schnulzen_image .
```
5. Create and run Docker Container, by inserting the current path (e.g. "/Users/bukold/Desktop/yt_schnulzen")
```
$ docker run -p 8888:8888 -v {path}:/home/jovyan my_schnulzen_image
```
6. Use the Skript by inserting URL into Webbrowser


Notes:
- You can use $pwd to find the current path
