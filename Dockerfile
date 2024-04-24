
# Используем образ Python последнюю версию
FROM python:latest

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в текущую директорию внутри контейнера
COPY . /app

# Устанавливаем зависимости Python из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт, который будет использоваться для Streamlit
EXPOSE 8501

# Команда запуска Streamlit приложения
CMD ["streamlit", "run", "streamlit_app.py"]

