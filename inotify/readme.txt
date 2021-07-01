uname -a output Linux 3.10.0-1160.21.1.el7.x86_64 #1 SMP Tue Mar 16 18:28:22 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

# to install inotify-tools
pbrun beroot
 yum update
 yum -y install epel-release
 yum repolist
 yum install inotify-tools

Python helper module: Not strictly required. Just used here to demonstrate capability of inotify-tools
https://pypi.org/project/inotify/
pip3.6 install inotify
pip3.6 install pulsar-client
pip3.6 install fastavro

python3.6 inotifyScript.py


