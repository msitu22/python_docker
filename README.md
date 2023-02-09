# python_docker

#### 1. Create a directory with a name "python-docker"
`
mkdir python_docker
`
#### 2. Navigate to the newly created directory
`
cd python_docker
`
#### 3. Create a virtual environment
##### Windows
`
py -3 -m venv venv
`

#### macOS/Linux

`
python3 -m venv venv
`

#### 4. Activate the environment
##### Windows

`
venv\Scripts\activate
`
##### macOS/Linux

`
. venv/bin/activate or source venv/bin/activate
`
#### 5 .Install Flask
`
pip install Flask
`

#### The service 1 will run on port 5000, and the service 2 will run on port 3000.
#### 6 .Build Docker image for serivce 1 with its Dockerfile:
`
cd sv1
docker build -t python-docker .
`
#### 7 .Build Docker image for serivce 2 with its Dockerfile:
`
cd sv2
docker build -t python-docker-2 .
`
##### when running docker images you should see the two images:
![image](https://user-images.githubusercontent.com/112602900/217962562-82f0a436-805f-455b-b39a-fe5ae1480fc8.png)

#### 8 . Setup Docker Network:
`
docker network create cdb-net
`
##### when running docker network inspect cdb-net you should see below:
![image](https://user-images.githubusercontent.com/112602900/217963264-fc51dd95-09b0-4828-8784-51c92005b6bc.png)

## Connect 2 Microservices:
#### 9 . Add Docker service 1 Container to the Docker Network cdb-net and run the container:
`
cd sv1
docker run -p 5000:5000 --network=cdb-net --name container python-docker
`
#### 10 . Add Docker service 2 Container to the Docker Network cdb-net and run the container:
`
cd sv2
docker run -p 3000:3000 --network=cdb-net --name container2 python-docker-2 
`
##### when running docker network inspect cdb-net now, you should see the 2 services docker containers have been added in the same network:
![image](https://user-images.githubusercontent.com/112602900/217963447-46e7713d-9352-48ad-8d4a-06d10df4b7a4.png)

#### 11 . Verify Docker containers can communicate
`
curl http://127.0.0.01:5000/Sunnyvale
`
##### when you type in city name(ex:Sunnyvale) after 5000/, you will the below result:
![image](https://user-images.githubusercontent.com/112602900/217963677-39d5cdac-a4cb-49b3-905f-4940d98f8199.png)



