FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY app.py /
COPY sitio.db /
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]