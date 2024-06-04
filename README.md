# Notes: BOILER PLATE PROCESS/TEMPLATE

1. open git bash terminal

2.  
```
git init
```

```
git add abc.txt

git add .
```

```
git commit -m "my commit"
```

or
We can use the source code GUI approach > 1. press on plus (+ stage change) > 2. commit message > publish (only 1st time) /sync changes / else tick mark -> the code will go to github 


3. in github > add file > create new file > .gitignore > template:python > save changes
4. in github > add file > create new file > LICENSE > choose the license type > MIT > commit changes

pandas -> BSD 2 License
tensorflow -> Apache License

5. 
```   
git pull
```
6. init_setup.sh -> If I dont want execute all the commands in bash manually, I can use init_setup.sh -> here i can put code for creating the environment, requirements.txt can be downloaded (only used for Linux, can be done using bash/gitbash)
Using the above I can automate the steps.

7. To run the commands in the init_setup.sh we have to run (in git bash terminal)

```
bash init_setup.sh
```

To see shell scripting see tutorialspoint.com/unix/shell_scripting.htm

8. To see the packages in the base, use

```
pip list
```

9. Sometimes in cases of errors we have to manually activate the environment

```
source activate ./env
```

10. Creating folder structure for the project : this is automated (for every project)

ML Project : 
a. Data Ingestion component
b. EDA comp
c. FE comp
d. Model Building comp
e. Evaluation comp

We will create pipeline
a. training
b. prediction

logger file -> for logging the information
exception file
utils file
setup.py -> used for storing local variables
requirements.txt
.gitkeep file -> when we created a folder in local (dev) and we want to push it form local to github
                 but in github we cannot push the empty folder. In that case we can keep those empty files .gitkeep
                 Initially in the yaml file we will keep the .gitkeep



Folder structure follow modular approach
|-.github/ - workflows/ (used for CICD) - yaml (we write the script/configuration here, where script available key value format)
|-Notebook/ - research.ipynb
|-src/ - Diamond_price_prediction/ - component/ - Data_ingestion.py, Preprocessing.py, model_training.py
|      - Pipeline/ - training.py, prediction.py
|      - exception.py
|      - logger.py
|      - utils.py
|-requirements.txt
|-setup.py

11. create template.py file
12. delete the init_setup.sh


Path(filepath) # it will generate system compatible path => doesnt depend on what we are providing

13. delete the init_setup.sh as we will create it using the template file
14. In the terminal run (for industry)

```
python template.py
```

15. __init__.py 

folder - package -> has many modules and withing it we have class and def
file - module or .py

from tensorflow.tensor import mytensor
from folder or package . file or module import class

we can create our own package also
|-Folder/
|-      module (.py) + __init__.py
|-                  class/def

the __init__.py justifies a folder as a package
In virtual environment -> pandas -> pip install pandas
                          custom/local package -> 1. pip install .
                                                  2. -e .
                                                  3. setup.py (python setup.py install)

In Python we test packages

16. update the setup.py file
17. delete the env folder
18. update the requirements.txt
19. update the init_setup.sh
20.   
```
bash init_setup.sh
```

If the environment is not activated by default, -> (some issue with windows)
```
source activate ./env 
```
can be used

21. 

# 1st way -> 
to see the custom/local package in pip list

```
python setup.py install
```

we will see the DiamondPricePrediction file in the pip list

$pip list
Package                Version
---------------------- -----------
DiamondPricePrediction 0.0.1             (This one)
joblib                 1.4.2
numpy                  1.24.4
pandas                 2.0.3
pip                    24.0
python-dateutil        2.9.0.post0
pytz                   2024.1
scikit-learn           1.3.2
scipy                  1.10.1
setuptools             69.5.1
six                    1.16.0
threadpoolctl          3.5.0
tzdata                 2024.1
wheel                  0.43.0


We will see several files created

* The author can give us the package , then author can deploy the project to pypi and then ask us to download from pypi

This is the first way to install custom  packages
Delete build, dist, egg file
```
pip uninstall DiamondPricePrediction
```

```
pip list
```

# 2nd way ->
open the requirements.txt

-e .    (-e -> editable)

```
pip install -r requirements.txt
```
We can again see the egg file

pip list

$ pip list
Package                Version     Editable project location
---------------------- ----------- ------------------------------------------------------------
DiamondPricePrediction 0.0.1       d:\python (full stack)\ineuron self practice\fsds_end_to_end \n
joblib                 1.4.2\n
numpy                  1.24.4\n
pandas                 2.0.3\n
pip                    24.0\n
python-dateutil        2.9.0.post0\n
pytz                   2024.1\n
scikit-learn           1.3.2\n
scipy                  1.10.1\n
setuptools             69.5.1\n
six                    1.16.0\n
threadpoolctl          3.5.0\n
tzdata                 2024.1\n
wheel                  0.43.0

  setup.py is mandatory for using the local packages without it putting  -e . would give error


# 3rd way(the best way)-
Thus using the setup.py we can even install the local as well as external packages.  

* The pip install -r requirements.txt in the init_setup.sh will take care of all the installations, as we have done all the setting in it using the get_requirements function and specifying the in install_requires argument of setup function


https://www.youtube.com/watch?v=Rv6UFGNmNZg


* We can use cookie cutter template also in place of template.py -> Check Krish Naik video


22. Notebook implementation of Project

1st we write the code in the ipynb file in notebooks/research.py
then we convert the code to modular code

HDL and LLD

Data ingestion real time -> Database -> SQL/NoSQL
                                        S3/Azure Blob


Docker learning -> https://www.linkedin.com/learning/docker-for-data-scientists/what-you-should-know?autoSkip=true&resume=false


# When Data is large, say 70gb ---> ??


For plotting -> plotnine is the best


# 29th October'23 session -> component and pipeline implementation
# 4th Nov23 -> creating prediction and web api
# 5th Nov23 Deployment of machine learning project with complete CI-CD
# 18th Nov23 Introduction of MLOps
# Mlflow uses in end to end project


# torch -> Datacamp
# DL -> from FSDS + Master GENAI


# CICD

|<--------Automated--------->
DEV -> Testing (pytest) : unittest/Integration -> QA 
|<--------------------CI--------------------------->


-> Deliver (Docker) -> Deployment -> monitoring and maintenance
|<<<<<<<<<<<<<<<<<<<<<      CD         >>>>>>>>>>>>>>>>>>>>>


local (dev env)  -> github -> github action (server) -> docker image -> AWS ECR / Az Container Repo -> AWS App Runner -> Server
-> deploy -> end point URL


CI = local (dev env)  -> github -> github action (server)
CD = docker image -> AWS ECR / Az Container Repo ->
CD =  AWS App Runner -> Server-> deploy -> end point URL

Self hosted Runner

------------------CICD or MLOPS ----------------------------
1. code available in local dev env
2. from here we are using git to push to github (central repo)
3. github action is an alternative of circleci/jenkins/travisci
   It is a server. server is nothing but a system. There are tools for CICD. On github action we would be running the docker file and creating docker image
4. The image will be pushed to ECR. Here we will save the docker image.
5. We will deploy the code to AWS App runner. In backend it will provide EC2.

