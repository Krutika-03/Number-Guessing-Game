FROM python:3
ADD main.py .
CMD ["python","-u","main.py"]