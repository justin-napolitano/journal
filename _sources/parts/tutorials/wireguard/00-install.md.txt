# Install Wireguard Rocky Linux 8

## Add EPEL Releases


:::{code-block} Bash
dnf install epel-release elrepo-release -y

:::

## Install WireGuard Packages

:::{code-blockk} Bass

dnf install kmod-wireguard wireguard-tools

:::

## Configuring Wireguard

### Create Config Directory

:::{code-block} Bash

mkdir /etc/wireguard

:::

### Generate Private Public Key Pair

:::{code-block} Bash

wg genkey | sudo tee privatekey | wg pubkey | sudo tee /etc/wireguard/publickey 

:::


### Create Conf File

:::{code-block} Bash

sudo vim /etc/wireguard/tun0.conf

:::

### Paste into conf

:::{code-block} 

[Interface]
PrivateKey = Paste-Server-Private-Key
Address = 10.5.0.1/24 
ListenPort = 51820
SaveConfig = true

:::

### Enabling Ip Forwarding

#### Open the configuration file at 

:::{code-block} Bash

sudo nano /etc/sysctl.conf

:::


#### Paste the following at the end of the file:


:::code-block} 

net.ipv4.ip_forward = 1

:::


#### Load Changes

:::{code-block} Bash

sudo sysctl -p


:::


### Firewall Settings


sudo firewall-cmd --zone=public --add-port=51820/udp --permanent


sudo firewall-cmd --zone=internal --add-interface=tun0 --permanent


#### Masqurading 

sudo firewall-cmd --zone=public --add-rich-rule='rule family=ipv4 source address=10.8.0.0/24 masquerade' --permanent
sudo firewall-cmd --zone=public --add-rich-rule='rule family=ipv6 source address=fd0d:86fa:c3bc::/64 masquerade' --permanent



#### rRelaoding

sudo firewall-cmd --reload





