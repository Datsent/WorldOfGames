FROM python:3.7
WORKDIR /wog
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
