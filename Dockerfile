FROM ubuntu:18.04 
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt ./requirements.txt
RUN mkdir -p ./Barco
COPY Barco ./Barco
WORKDIR ./Barco
CMD python3 -m pytest -v /Barco/warrantyinfo_testcase_results.xml warrantyinfo_testcase.py

# How to Use
# docker build -t <image name> -f <Dockerfile path>.
# docker run -it --name <container nane> <image name>
# docker cp <image name>: <container_path.xml> ./<local_path.xml>
# docker rm -f <remove container>
