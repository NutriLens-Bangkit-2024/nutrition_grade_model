# NutriLens Grade Models

## Running the Models

These steps will guide you through setting up the environment, installing dependencies, and running the NutriLens Grade Models.

### **1. Set Up the Environment**

* Install `virtualenv`:

```bash
pip install virtualenv
```
* Set the python version:
```bash
virtualenv --python=python3.10 .venv
```
* Create Environment
```bash
python -m venv .venv
```
* Activate the Environment
```bash
.venv\Scripts\activate
```
* Deactivate the Environment
```bash
deactivate
```


### **2. Install the required dependencies** 
```bash
pip install -r requirements.txt
```
### **3. To Run the docker, make sure you have installed Docker Desktop**
### **4. Once Docker Desktop is installed, run this command**
```bash 
docker build -t nutriscore-app .
```
Note : nutriscore-app can be changed into any name you like
### **5. After building, run this command**
```bash
docker run -p 80:80 nutriscore-app
```
### **6. You can now access the docker by going to your browser and type:** ***localhost/docs or 0.0.0.0/docs***
```text
localhost/docs
```
or
```text
0.0.0.0/docs
```
