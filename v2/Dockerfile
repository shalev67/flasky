
FROM ubuntu:14.04
MAINTAINER Yuval Shalev "shalev67@gmail.com"
COPY . /tmp
WORKDIR /tmp
RUN sudo apt-get update && sudo apt-get install -y --force-yes python-pip python-dev
RUN sudo pip install flask
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]
