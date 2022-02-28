# Configuraing Conda For Data Science

## Installation 

Navigate to [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) to download conda for your system. 

## Initial Configuration 

I typically begin my configuration by creating a data science virtual envioronment.  To begin this section of the tutorial open a terminal window. 

### Update Conda
 
Before you create your environment or download any packages update you conda environment.

:::{code-block} Bash

conda update conda

:::


### Create Your Venv

Now create a virtualenv.  You may name it whatever you want.  I will call mine data-science.  I will also choose python 3.9 as my python version.  



#### Syntax

Below is the syntax to create the environment.  

:::{code-block} Bash

conda create -n <yourenvname> python=<x.x> anaconda


:::


#### Run

Below is the syntax to create the environment.  

:::{code-block} Bash

conda create -n data-science python=3.9 anaconda


:::

