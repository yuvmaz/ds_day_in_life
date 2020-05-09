FROM python:3.7.7-slim-buster

RUN apt-get update && apt-get install -y build-essential
RUN pip install pymc3 seaborn statsmodels jupyter
RUN mkdir -p /opt
WORKDIR /opt

ADD day_in_the_life.ipynb .
ADD data.csv .

EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''","--NotebookApp.password=''"]

