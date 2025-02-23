FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3
RUN pip3 install flask gunicorn
COPY app.py /opt/
WORKDIR /opt
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
