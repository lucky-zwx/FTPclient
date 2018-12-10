from ftplib import FTP
import ftplib
import sys

bufsize = 1024
user = ''
password = ''
host = '127.0.0.1'
filepath = ''


def filelist():
    global num
    print(ftp.dir())
    d_filelist = input("输入你想进入的目录")
    ftp.cwd(d_filelist)

def download(d_filename, file):
    fp = open(file, 'wb')
    ftp.retrbinary('RETR ' + d_filename, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close

for login in range(0, len(sys.argv)):
    if sys.argv[login] == '-u':
        user = sys.argv[login+1]
    if sys.argv[login] == '-p':
        password = sys.argv[login+1]
    if sys.argv[login] == '-h':
        host = sys.argv[login+1]
    if sys.argv[login] == '-f':
        filepath = sys.argv[login+1]

try:
    ftp = FTP()
    ftp.encoding = 'utf-8'
    ftp.connect(host)
    ftp.login(user=user, passwd=password)
    while (True):
        lnum = input('0.查看目录   1.下载    (输入序号进行操作)\n')
        if lnum == '0':
            filelist()
        if lnum == '1':
            d_filename = input('请输入文件名： \n')
            file = input('请输入本地文件：  \n')
            download(d_filename=d_filename, file=file)
    ftp.quit()
except BaseException:
    for errormes in ftplib.all_errors:
        print(errormes)
