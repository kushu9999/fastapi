FROM python

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
&& pip install -r requirements.txt

# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

# EXPOSE 8080
