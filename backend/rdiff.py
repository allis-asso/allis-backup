from subprocess import check_call 

class rdiff:
    @staticmethod
    def backup( source, destination):
        check_call( ['/usr/bin/rdiff-backup', source, destination])

