# NutriLens Grade Models

## Follow this steps to run this models
1. Setup The Env  
`windows -> venv\Scripts\activate`
2. Install the required dependencies `pip install -r requirements.txt`
3. To Run the docker, make sure you have installed Docker Desktop
4. Once Docker Desktop is installed, run this command `docker build -t nutriscore-app .`
Note : nutriscore-app can be changed into any name you like
5. After building, run this command `docker run -p 80:80 nutriscore-app`
6. You can now access the docker by going to your browser and type localhost/docs or 0.0.0.0/docs
