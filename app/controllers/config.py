import re

RELEASE = 'C:/_SERVIDOR/'
DBSRV = RELEASE + 'DBSrv/run/'
TMSRV = RELEASE + 'TMSrv/run/'
COMMON = RELEASE + 'Common/'

def getInitial(account):
    if (re.search(r'[A-Za-z]+', account[0])):
        return account[0]
    else:
        return 'etc'