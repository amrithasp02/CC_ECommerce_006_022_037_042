FROM jenkins/jenkins:lts
#FROM ubuntu:20.04
# if we want to install via apt
USER root
RUN apt-get update && apt-get install -y make && apt-get install -y g++ python3-dev --fix-missing
# drop back to the regular jenkins user - good practice
USER jenkins






