FROM python:latest
WORKDIR /etl
ADD requirements.txt requirements.txt
ADD rutas.py rutas.py
COPY crear_tabla.py
CMD ["python","crear_tabla.py"]