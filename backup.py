#! /usr/bin/python3
from datetime import date
from fs import btrfs
from backend import rdiff

today = date.today()

snap_name = '/snapshots/snap-%d%02d%02d' % (today.year, today.month, today.day)
volume = "/"
destination = "backup_client@backup::/home/backup_client/backup"

# make a snapshot
btrfs.snapshot( volume, snap_name);


# backup the snapshot
rdiff.backup( snap_name, destination)

# handle snapshot rotation

