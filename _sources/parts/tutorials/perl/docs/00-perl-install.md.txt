(perl_install)=
# Perl Installation 

Perl is a dependency for many install scripts, especially older ones.  

It is often shipped with the system.

## Debian/Ubuntu Install

### Update your packages

:::{code-block} Bash
sudo apt update && sudo apt upgrade

:::

### Install Perl 

:::{code-block} Bash
sudo apt install perl
:::

## RHEL, Cent, Rocky

### Update

:::{code-block} Bash

sudo dnf update -y

:::

### Install Perl dnf

:::{code-block} Bash
# use the -y flag to install dependencies

sudo dnf install perl -y
:::


## MacOs

### Brew install

:::{code-block} Bash
brew install per
:::