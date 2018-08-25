# Machines

## Add new Admin Setup
In order to add a new admin, a set of tasks need to be performed, both on the servers side (both machines) and client side (new user)
Note that only a sudoer is able to add new admins.

### Server

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

### Client
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
- the setup is done, exit

## Automation Services

Several utilities are used in order to assure the best possible 

### Updates

### Snapshots
