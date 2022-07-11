# Student-management-system-backend
This is the student management system made with python using django framework. default superuser is username: dipesh password: dipesh
This is an backend made with django rest framework.  I have implemented jwt for the authentication.
The interface of the api would be like this: 
![image](https://user-images.githubusercontent.com/63381568/178244021-5d60c50b-e3ef-47e2-9096-a7b5bf3163b5.png)

In order to perform CURD operation you must have to be admin or super user.
Student list
![image](https://user-images.githubusercontent.com/63381568/178244394-4123f96f-d0df-4e25-940e-fe9120c10475.png)
Grade list
![image](https://user-images.githubusercontent.com/63381568/178244496-ebeabdfb-2eb9-4b56-bb63-d56fe5ea34dd.png)

The end point are as follow: 
Basic end point:
http://127.0.0.1:8000/students/ => to get student list and if you are admin you can add or remove students
http://127.0.0.1:8000/grades => to get grade list and if you are admin you can add or remove grade

Auth End point: 
http://127.0.0.1:8000/auth/users/ => to register a user 
![image](https://user-images.githubusercontent.com/63381568/178245017-e1a7392c-0a1e-44dd-b80e-4069f74c9f13.png)

http://127.0.0.1:8000/auth/jwt/create => to login a user and get jwt token for authentication
![image](https://user-images.githubusercontent.com/63381568/178245124-7e56de9c-3d23-4aa2-9f00-2b03f2a64d46.png)
