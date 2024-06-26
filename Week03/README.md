# End-to-End Data Portfolio 03

Episode 3 of Josh Dev's First End-to-End Data Portfolio series.

* Setting up a WSL (Windows Subsystem for Linux).
* Setting up the FTP server.
* Connecting to the FTP server and establishing a secure connection.
* Creating a pipeline for downloading, uploading, and deleting data.
* The pipeline involves downloading from the URL, uploading to the FTP server, and deleting files locally.
* Adding parameters for manual or scheduled execution.

# Notes for myself
* `sudo su`, Root Access
* `apt update && apt upgrade`
    * apt (make changes to Ubuntu)
    * update (find updates)
    * && (and)
    * upgrade (install the updates)


## Setting-up WSL

* Open PowerShell as an administrator.
* Run `wsl -l -o` to see available distros that can be installed.
* Run `wsl --install` to install the default distro (Ubuntu).
    * To select a different distro, run `wsl --install -d <Distribution Name>`.
* You may need to restart your device after installation for the changes to take effect.
* You are now prompted to create a new user. Enter your username and set a password.

## vsftpd Configuration

* `ls /etc/` to locate the vsftpd.conf file.
* `cp /etc/vsftpd.conf /etc/vsftpd.conf_original` to create an original copy of the file.
* `nano /etc/vsftpd.conf` nano is a text editor so we can edit the file
* `systemctl restart vsftpd`
* `systemctl status vsfpd`
* `touch /etc/vsfpd.chroot_list` create a blank list of users for chroot
