
#исходник
# # Используем образ Python версии 
# FROM python:latest

# # Устанавливаем рабочую директорию внутри контейнера
# WORKDIR /app

# # Копируем файлы проекта в текущую директорию внутри контейнера
# COPY . /app

# # Устанавливаем зависимости Python из файла requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Добавьте ваше приложение в Docker образ
# ADD server.py /app/server.py
# ADD streamlit_app.py /app/streamlit_app.py

# # Установите рабочую директорию
# WORKDIR /app

# # Откройте порт, который будет использоваться вашим сервером FastAPI
# EXPOSE 8000

# # Запускаем сервер FastAPI и streamlit_app.py параллельно с помощью & в конце каждой команды
# #CMD uvicorn server:app --host 0.0.0.0 --port 8000 && streamlit run streamlit_app.py

# # Команда запуска обоих сервисов параллельно
# CMD ["bash", "-c", "uvicorn server:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py"]

# до вот этого 

# Запустите сервер FastAPI при запуске контейнера
#исходник внизу  работающий локально
#CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
# хз следующий внизу 
# # Используем базовый образ Python 3.9
# FROM python:3.11



# Используем образ Python версии 
FROM python:latest

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в текущую директорию внутри контейнера
COPY . /app

# Устанавливаем зависимости Python из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Откройте порт, который будет использоваться вашим сервером FastAPI
EXPOSE 8000
EXPOSE 8501

# Команда запуска обоих сервисов параллельно
CMD ["bash", "-c", "uvicorn server:app --host 0.0.0.0 --port 8000 & streamlit run --server.port 8501 streamlit_app.py"]
