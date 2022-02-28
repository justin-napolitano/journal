# Configuring Jupyter For Data Science

## Installation 

:::{code-block} Bash

pip3 install jupyter

:::

## Initial Configuration 

I typically begin my configuration by creating a data science virtual envioronment.  To begin this section of the tutorial open a terminal window. 


### Create Your Venv

Now create a virtualenv.  You may name it whatever you want.  I will call mine data-science.  I will also choose python 3.9 as my python version.  



#### Command

Below is the syntax to create the environment.  

:::{code-block} Bash

virtualenv /path/to/venvs/ <name of venv>

:::



### Activate your Venv

:::{code-block} Bash
source /path/to/venvs/name of venv/bin/activate
:::

### Configure ipython kernal to enable jupyter to use your environment

:::{code-block} Bash
ipython kernel install --user --name=nameofvenv

:::


## Running Jupyter with your environment

Start an instance of jupyter notebook.

Select kernal from the dropbown menu and select your new venv kernal.


View the screenshot below.

![Screen Shot](/_static/pictures/jupyter-kernal-select.jpeg)