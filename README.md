
---

# Прогнозирование технического обслуживания

## Описание проекта

Этот проект представляет собой веб-приложение для прогнозирования технического обслуживания оборудования с использованием машинного обучения. Приложение предназначено для предсказания поломок оборудования на основе различных параметров процесса, таких как температура, обороты, крутящий момент и износ инструмента. Также проект включает чат-бота **NGMK GPT**, использующего модели **Ollama 3.1**, **3.2** и **3.3**, для интерактивного взаимодействия с пользователем.

Проект был разработан для **Навоийского горно-металлургического комбината (НГМК)**, с целью оптимизации процессов технического обслуживания и минимизации времени простоя оборудования.

## Структура проекта

- **app.py** – основной файл приложения на Streamlit.
- **ML models** – обученные модели для прогнозирования поломок оборудования.
- **Dockerfile** – файл для создания контейнера Docker.
- **requirements.txt** – список зависимостей для проекта.
- **ngmk_gpt_bot** – чат-бот на базе модели NGMK GPT.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/Predictive-Maintenance.git
   cd Predictive-Maintenance
   ```

2. Установите зависимости:

   Для установки зависимостей можно использовать виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Для работы с Docker:

   Сначала создайте Docker-образ:

   ```bash
   docker build -t predictive-maintenance .
   ```

   Затем запустите контейнер:

   ```bash
   docker run -p 8501:8501 predictive-maintenance
   ```

4. Запустите приложение с помощью Streamlit:

   ```bash
   streamlit run app.py
   ```

## Использование

1. **Прогнозирование поломок**: Введите параметры процесса (температуру, обороты, крутящий момент и т.д.) в форму, и модель предскажет, произойдет ли поломка и какого типа она будет.
2. **Чат-бот**: Воспользуйтесь чат-ботом для получения дополнительной информации о состоянии оборудования и прогнозах, а также для общения по вопросам обслуживания.

## Архитектура

Проект включает следующие компоненты:

- **Frontend**: Веб-приложение на Streamlit, которое предоставляет интерфейс для ввода данных и отображения результатов.
- **Machine Learning Model**: Модели для прогнозирования поломок оборудования, использующие машинное обучение.
- **Docker**: Используется для упаковки приложения и его развертывания.
- **CI/CD**: Автоматизация развертывания с помощью GitHub Actions.
- **Huggingface Space**: Развертывание приложения в облаке для обеспечения масштабируемости.

## Технологии

- **Python 3.x**
- **Streamlit**
- **Docker**
- **Machine Learning** (пакеты: scikit-learn, pandas, numpy, и др.)
- **Huggingface Spaces**
- **Ollama Models 3.1, 3.2, 3.3** (для чат-бота)

## Планы на будущее

- Добавление интеграции с реальными источниками данных.
- Расширение возможностей чат-бота для поддержки дополнительных запросов.
- Улучшение точности моделей с использованием дополнительных данных и методов машинного обучения.

## Лицензия

Этот проект использует лицензию MIT.

---
