FROM python:3.8
 
WORKDIR /app
 
ADD . /app
 
RUN pip install -r requirements.txt

RUN python create.py
CMD python main.py