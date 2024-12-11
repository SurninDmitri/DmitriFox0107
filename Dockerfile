# Используем официальный образ Python
FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    curl \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl -sSL https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
    msodbcsql17 \
    unixodbc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска приложения
CMD ["flask", "run", "--host=0.0.0.0"]