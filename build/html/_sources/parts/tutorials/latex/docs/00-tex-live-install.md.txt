# Installing Tex Live

## Dependencies.  

You will need perl to install. Go to {ref}`perl_install` for instructions.

You may also need development tools for your distribution.  Go to {ref}`development-tools` for instructions.

## Linux and Nix Systems

### Download the installer.

First download the TexLive Installer from a mirror. The standard download mirror location is [https://mirrors.mit.edu/CTAN/systems/texlive/tlnet/](https://mirrors.mit.edu/CTAN/systems/texlive/tlnet/). 

I typically download to an image or config directory in my home file.  

:::{code-block} Bash
#cd to the download directory of your choice.  I use images in my case

cd ~/images

:::


:::{code-block} Bash
#download the tarball

wget https://mirrors.mit.edu/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz

:::

### Expand the Tarball

:::{code-block} Bash
#Expand

tar -xvzf install-tl-unx.tar.gz

:::


### Run the installer

I found that it is necessary to run the installer with root priveleges so that it can create symlinks and write to the sur directory. 

:::{code-block} Bash
# cd to the install directory

cd <path to unzipped file>


## Run the installer and follow the instructions

sudo perl install-ls

:::


Be patient it may take upwards of an hour to install the entire distribution. 
