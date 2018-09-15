# Eden Box

## Description
This document summarizes all knowledge needed in order to redeploy and maintain the existing Eden Box project components, while requiring only basic Linux and
sysadmin knowledge, easily acquirable online.

## Outline
The project relies upon two Ubuntu virtual machines, both provided by [Okeanos-Global](./services/okeanos.md).
Both machines automatically update daily at 2 am, using a cron job running apt-get package manager.  
Additionally, the machines create a snapshot of their current state twice a month (1st and 15th) and upload it to the Okeanos [Pithos](./services/okeanos.md#pithos) service, in order to provide recoverability means in case of severe failure of the VMs.
Given that Pithos' capacity is limited, these snapshots overwrite older ones so that, at a given time, only 6 distinct snapshots of a machine are stored in the cloud.

The machine with the role of file server, designated from here on as eden-fs, provides:
	* Nextcloud service, responsible for providing the file storage platform
	* Public interface to Nextcloud
	* Python log reader, responsible for detecting file access entries written to the Nextcloud log and sending them to the database

The machine with the role of database, designated from here on as eden-db, provides:
	* PostgreSQL database, responsible for saving timestamps of each file access on the server side
	<!--* TODO add Data Science capabilities information -->

For more information about the machines, please refer to [machines](./service/machines.md) section

Each of the admin members can access the machines through ssh authentication, solemnly to their own user, relying on pre-configured RSA keys, ad-hoc distributed to each of the users.
Note that the key used to authenticate a user is the same on both machines, which allows easier configuration at the expense of a more resilient security solution.
The safest option would require a key pair per-user for each machine, but it would be less pratical to manage.

## Deployment
More information is available on the [deployment](./deployment/) section. 

## Maintenance
Even though many maintenance steps have been suppressed through automation, there are still some tasks that require administrative attention and support. 
Please refer to the [maintenance](./maintenance/) section for more information.

## Security Concerns
Up to the available knowledge at the time of deployment, the best practices and concerns related to Cyber-security have been attended. However, the system's resilience to miscreants still relies on the most vulnerable link: its users. Therefore, extreme care is advised to admin users whilst handling private keys and database user certificates, as those possessing them are implicitly provided access to machines and are therefore able to undermine the system at will. Hence, under any circumstance should they grant access to third parties whose trust is not assured.

## Acknowledgments
All collaboration and commitment of those involved in this project is truly cherished and appreciated.

_"It must be considered that there is nothing more difficult to carry out nor more doubtful of success nor more dangerous to handle than to initiate a new order of things."_ - Machiavelli
