# Machines

## Add new Admin Setup
In order to add a new admin, a set of tasks need to be performed, both on the servers side (both machines) and client side (new user)
Note that only a sudoer is able to add new admins.

### Server
As a sudoer user,
// FIXME change this to new script usage 
- ```useradd <username>```
- ```cd /home/<username>/.ssh```
- Check if .ssh exists, ```ls -la```:
	- if not, ```mkdir .ssh && chmod 700 .ssh```
- ```cd .ssh```
- ```sudo vi authorized_keys```
- append the user public key
- // TODO continue
 
This procedure needs to be executed on both machines, eden-fs and eden-db.
<username> will represent the name intended for the user we intend to add.

- // TODO

### Client
Afterwards, the client side setup can be made as follows:

From a Linux system terminal,

Obs. keep in mind that
<username> -> your username on the remote machines, ex. rainbow
also, your current account password is on the zip's <username> password.txt (will be changed later)

- Access /home/username/ aka ~/
- Check if .ssh exists, ```ls -la```:
	- if not, ```mkdir .ssh && chmod 700```
- ```cd .ssh```
- add the eden_<username>.priv key to this directory
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
- Both eden-fs and eden-db will be the used alias to access the machines through ssh
- try to access the machines, ```ssh eden-fs``` and ```ssh eden-db```
- run the following command, in each machine, to change password, __please do not choose a weak password__, ```passwd```
- the setup is done, exit
