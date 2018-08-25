# Eden Box

## Description
This document summarizes all knowledge needed in order to redeploy and maintain the existing Eden Box project components, while requiring only basic Linux and
sysadmin knowledge, easily acquirable online.

## Outline
The project relies upon two Ubuntu VM machines, both provided by [Okeanos-Global](./services/okeanos.md).
Both machines automatically update daily at midnight, using a cronjob running apt-get package manager.  
Additionaly, the machines create a snapshot of their current state twice a month, 1st and 15th, and upload it to Okeanos [Pythos](./services/okeanos.md#pythos) service, in order to provide recoverability means in case of severe failure of the VMs.
Given that Pythos capacity is limited, these snapshots overwrite older ones so that, at a given time, only 6 distinct snapshots of a machine are stored on the cloud.

The machine with the role of file server, designated from here on as eden-fs, provides:
	* Nextcloud service, responsible for providing the file storage platform
	* public interface to Nextcloud
	* Python log reader, responsible for detecting file access entries written to the Nextcloud log and sending these updates to the database

The machine with the role of database, designated from here on as eden-db, provides:
	* Postgres database, responsible for saving access timestamps of each file access on the server side
	<!--* TODO add Data Science capabilities information -->

For more information about the machines, please refer to [machines](./service/machines.md) section

Each of the admin members can access the machines through ssh authentication, solemnly to their own user, relying on pre-configured RSA keys, ad-hoc distributed to each of the users.
Note that the key used to authenticate a user is the same on both machines, which allows easier configuration at the expense of a more resilient security solution.
The safest option would require a key pair per-user for each machine, but it would be less pratical to manage accesses.

## Deployment
More information is available on the [deployment](./deployment/) section. 

## Maintenance
Even though many maintenance steps have been suppressed through automation, there are still some tasks that require administrative attention and support. 
Please refer to he [maintenance](./maintenance/) section for more information.

## Security concerns
Up to the available knowledge at the time of deployment, the best practices and concerns related to Cyber-security have been attended. Yet, the system resilience to miscreants still relies on the most vulnerable link, users. Therefore, extreme care is advised to admin users whilst handling private keys and database user certificates, as those posessing them are implicitly provided access to machines and are therefore able to undermine the system at will. Hince, under any circunstance grant access to third parties whose trust is not assured.

## Acknowledgments
All collaboration and commitment of those involved in this project is trully cherished and appreciated.

_"It must be considered that there is nothing more difficult to carry out nor more doubtful of success nor more dangerous to handle than to initiate a new order of things."_ - Machiavell
