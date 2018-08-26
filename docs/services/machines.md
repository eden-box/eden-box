# Machines

## Add new Admin Setup
In order to add a new admin, a set of tasks need to be performed, both on the servers side (both machines) and client side (new user)
Note that only a sudoer is able to add new admins.

### Server

#### SSH
_Strictly follow the procedure without changing any file name during this process_

<username> will represent the name intended for the user we want to add

As a sudoer user,

Run script ```/usr/local/sbin/manageuser.sh``` at eden-fs,
- ```cd /usr/local/sbin```
- ```sudo manageuser.sh -c <username>```
Provide a minimally secure password when requested, during the procedure.
This password should later be changed by the new user, during it's first access to the machine.

Afterwards, a zip file with the required information for the new user to execute the needed ssh setup at his machine
will be present at the folder containing the script.

A similar setup now needs to be executed in eden-db.
Make sure that a public key <username>.pub is present on the same folder where the script is located.
- ```cd /usr/local/sbin```
- ```sudo manageuser.sh -u <username>```

Send the zip file to the new user which should be able to access both machines after he completes the ssh setup.

#### Okeanos-Global
After requesting the user to register himself in Okeanos-Global and registering a non-academic e-mail, use it for the following step.
From an admin Okeanos Account, access Pithos, 'Groups' and add the new user valid e-mail address to the 'edenbox' group.
The user is now able to access the existing machine images.

### Client

#### SSH
Afterwards, the client side setup can be made as follows:

From a Linux system terminal,

Obs. keep in mind that
<username> -> your username on the remote machines, ex. rainbow
also, your current account password is on the zip's <username> password.txt (will be changed later)

- access /home/username/ aka ~/
- check if .ssh exists, ```ls -la```:
	- if not, ```mkdir .ssh && sudo chmod 700 .ssh```
- ```cd .ssh```
- add eden_<username>.priv key to this directory
- using a text editor, edit/create file "config" and restrict access permitions ```touch config && sudo chmod 600 config```
- add the following entry:
```
Host eden-fs
	HostName 83.212.82.36

Host eden-db
	HostName 83.212.82.38

Host eden-fs eden-db
	User <username>
	IdentityFile ~/.ssh/eden_<username>.priv
```
- both eden-fs and eden-db will be the used alias to access the machines through ssh
- try to access the machines, ```ssh eden-fs``` and ```ssh eden-db```
- run the following command, in each machine, to change password, __please do not choose a weak password__, ```passwd```
- the setup is over, exit

#### Okeanos-Global
Access Okeanos-Global and sign-in through an academic login.
From 'Dashboard', add a valid non-academic e-mail address for ease of use purposes.
Share the used e-mail address with an admin user in order to finish the setup.
Afterwards, check if you have access to the resources.

## Automation Services

Several utilities are used on both machines in order to assure the best possible functionality of the service and reliability of the system.
Given that all scripts were registered using ```crontab -e``` one must take into account that they are run using _sudo_ privileges.

### Updates
Located in ```/usr/local/sbin/```, [update.sh](update.sh) is executed by a daily cronjob run at 2 a.m.
Using apt-get, package lists are update and and fetched. In case of linux headers update, the machine is rebooted in order to complete process. 

Usually, eden-db takes longer than eden-fs to update, it may be due to bad update mirror selection, further experimentation is required.

### Snapshots
Located in ```/usr/local/sbin/```, [backup.sh](backup.sh) is executed by cronjob run at the 1st and 15th day of each month, at 4 a.m.

In order for the script to work properly, the token needs to be updated monthly directly on the code.
Okeanos automatically renews the API token monthly and there is no way to automate this update process through code, therefore, an admin needs to update the script by hand.
