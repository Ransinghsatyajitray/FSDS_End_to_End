# Notes:

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