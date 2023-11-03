FROM python:3.10.12

WORKDIR /locust

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./locustfiles ./locustfiles
COPY ./common ./common
COPY ./utils ./utils
COPY ./.env .
RUN cd ./locustfiles & ls
RUN ls 
RUN pwd

CMD [ "sleep" , "infinity" ]