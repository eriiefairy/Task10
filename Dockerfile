FROM python
ENV PYTHONNUNBUFFERED=1
WORKDIR /code
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python","manage.py","runserver"]