# allis-backup
A remote backup management written in python


Creation nouveau client
=======================

installer btrfs-tools et rdidd-backup

Créer un dossier snapshots
mkdir /snapshots/

generer une clé SSH pour root sur le client: root@client
ssh-keygen 

generer un utilisateur sur le serveur
ssh backup
adduser backup_client
CTRL-D

Copier la clé SSH de root sur le serveur
ssh-copy-id backup_client@backup

Corriger le nom d'utilisateur dans le script backup.py (et le home de destination !!)

Generer un crontab
0 1 * * * /root/backup_script/backup.py

