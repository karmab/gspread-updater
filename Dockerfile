FROM centos:7
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN yum -y install git epel-release && yum -y install python-pip && yum clean all && rm -rf /var/cache/yum
RUN pip install gspread

ADD update.py /usr/bin

RUN chmod o+x /usr/bin/update.py

ENTRYPOINT ["/usr/bin/update.py"]
