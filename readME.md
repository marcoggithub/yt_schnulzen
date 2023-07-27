## Usage:
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
6. Use the Skript by inserting URL into Webbrowser - I recommend the URL using http://127.0.0.1:8888. Your Terminal should show something like this:
```
To access the server, open this file in a browser:
    file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
Or copy and paste one of these URLs:
    http://bea402ca72f5:8888/lab?token=dfb6c11db730a040fd85a7c2c250666ce93e2cd63b7f7fa0
    http://127.0.0.1:8888/lab?token=dfb6c11db730a040fd85a7c2c250666ce93e2cd63b7f7fa0
```
7. Now you are ready to use the main.ipynb script or train an model with the scripts under "/bert"

Best of Luck,\
Q.

Notes:
- You can use $pwd to find the current path
