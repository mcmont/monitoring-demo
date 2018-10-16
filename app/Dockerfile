FROM frolvlad/alpine-python3
COPY app/requirements.txt /requirements.txt
COPY app/app.py /app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]