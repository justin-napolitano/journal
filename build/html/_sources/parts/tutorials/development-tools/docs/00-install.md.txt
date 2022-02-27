(development-tools)=

# Development Tools Installation

It is good practice to update your system prior to install.  Start by running your distro's update procedures.  

## Rhel, Cent, Rocky


### List your available groups.


:::{code-block} Bash

dnf group list

:::

### Install the Development Tools group.  It is case sensitive. 


:::{code-block} Bash

dnf group install 'development tools'

:::


## Ubuntu

### Install Build Essentials

:::{code-block} Bash

sudo apt-get install build-essential

:::

## MacOS

### Install X-Code CLI Tools and Build Tools

Run the following command in your terminal emulator to initialize the install. 

:::{code-block} Bash

xcode-select --install

