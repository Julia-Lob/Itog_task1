FROM python:3.9

ENV my_dir=r'/home/julia/PycharmProjects'

WORKDIR /usr/src/app

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Настраиваем команду, которая должна быть запущена в контейнере во время его выполнения
ENTRYPOINT ["python", "./app.py"]

#CMD ["python", "./app.py", ""]