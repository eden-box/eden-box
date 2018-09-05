# Logrotate
Configuration files of the logrotate utility.

## Description
Brief outline of the how's and why's of the employed configuration files.

### Backup
Attempt to rotate the log each day, but only if it is not empty.
Method used in order to avoid finer grained treatment based on date analysis.

### Update
Keeps the last 4 weeks of update logs, compressed.
The log file is rotated weekly.

### Final Notes
Logrotate allows automatical cleanup of old logs, therefore, avoiding the need
of manual management of all of the generated files.
