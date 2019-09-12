## Build from Ubuntu 16.04 base image
FROM ubuntu:16.04

## Disable Interaction
ENV DEBIAN_FRONTEND noninteractive

## Update the image
RUN apt-get clean && \
    apt-get update -y && \
    apt-get upgrade -y

## Install our dependencies
RUN apt-get install python3-pip -y && \
    apt-get install libmysqlclient-dev -y

## Install the requirement Python3 modules
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

## Copy the Flask App source files
COPY shared.py template.py template.cfg boot.sh /usr/src/app/
COPY models /usr/src/app/models
COPY resources /usr/src/app/resources

## Give the boot script run permissions
RUN chmod +x /usr/src/app/boot.sh

## Set out exposed port
EXPOSE 5000

## Run out boot script
ENTRYPOINT ["./usr/src/app/boot.sh"]
