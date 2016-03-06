from subprocess import check_call 
import os.path

class btrfs:
    @staticmethod
    def snapshot( subvolume, snapshot_name):
        snapshot_folder = os.path.dirname(snapshot_name)
        if not os.path.isdir( snapshot_folder):
            os.makedirs( snapshot_folder)
        check_call( ['/sbin/btrfs', 'subvolume', 'snapshot', subvolume, snapshot_name])

