FROM python:3.6
RUN useradd -ms /bin/bash flask
USER flask
WORKDIR /app
COPY . /app

RUN pip install --user -r requirements.txt
CMD ["python", "__init__.py"]