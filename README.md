# allis-backup
A remote backup management written in python


Add a client to the system
==========================
Install btrfs-tools et rdiff-backup

    apt-get install btrfs-tools rdiff-backup

Create the snapshots directory:

    mkdir /snapshots/

Generate SSH key for root on the client: root@*client*

    ssh-keygen 

Create a user on the server

    ssh backup
    adduser backup\_*client*
    CTRL-D

Copy the root SSH key on server

    ssh-copy-id backup\_*client*@backup

Fix the user name in the script backup.py (and the the home destination path !!)

Generate a crontab

    0 1 * * * /root/backup\_script/*backup.py

