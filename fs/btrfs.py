from subprocess import check_call 

class btrfs:
    @staticmethod
    def snapshot( subvolume, snapshot_name):
        check_call( ['/sbin/btrfs', 'subvolume', 'snapshot', subvolume, snapshot_name])

