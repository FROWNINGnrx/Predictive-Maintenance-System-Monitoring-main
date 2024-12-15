import streamlit as st
import io
import subprocess
import requests
import streamlit.components.v1 as components
from annotated_text import annotated_text
from src.Predictive_Maintenance.pipelines.prediction_pipeline import prediction

# Устанавливаем конфигурацию страницы в самом начале
st.set_page_config(layout='wide')

# Фон и стилизация страницы
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("static/Fon.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .css-1v3fvcr {
        background-color: #f2f2f2;
    }

    /* Стилизация кнопок */
    .stButton>button {
        background-color: #80c5f7;  /* Светло-синий фон */
        color: white;  /* Белый цвет текста */
        font-size: 16px;
        padding: 12px 20px;  /* Увеличенные отступы для кнопки */
        border-radius: 8px;  /* Закругленные углы */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Тень */
        transition: background-color 0.3s ease, transform 0.3s ease;  /* Плавный переход */
        cursor: pointer;
        border: none;
    }

    .stButton>button:hover {
        background-color: #5ba0e6;  /* Темно-синий при наведении */
        transform: translateY(-2px);  /* Немного поднимаем кнопку при наведении */
    }

    .stButton>button:active {
        background-color: #428bca;  /* Более темный синий при клике */
        transform: translateY(2px);  /* Кнопка слегка "проваливается" при клике */
    }

    /* Для блокировки перехода между разделами */
    .css-1kyxreq {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)


# Логотип в боковой панели
st.sidebar.image("static/logo.svg", use_container_width=True)

# Навигация в боковой панели
with st.sidebar:
    st.title("Техническое Обслуживание")
    choice = st.radio(
        "Выберите одну из опций:",
        ["Главная", "EDA", "Отчёты по мониторингу", "Оценка производительности", "Прогнозирование", "NGMK GPT"]
    )

# Главная страница
if choice == "Главная":
    with open("frontend/main/main_page.md", "r", encoding="utf-8") as file:
        readme_contents = file.read()
    st.markdown(readme_contents)

# Страница EDA
if choice == "EDA":
    st.title('Исследовательский Анализ Данных')

    st.header('Вопрос 1')
    st.write("Каково распределение метки 'машинный отказ' в наборе данных? Сколько случаев отказа и сколько нет?")
    st.image("reports/q1.png", use_container_width=True)
    st.write("**Успешность работы машины составляет 96.52%, а наибольший тип отказа - это HDF (Ошибка теплоотведения) с коэффициентом отказа 1.15%.**")

    st.header('Вопрос 2')
    st.write("Каково распределение переменной 'productID' в наборе данных? Сколько случаев для низкокачественных, среднекачественных и высококачественных вариантов?")
    st.image("reports/q2.png", use_container_width=True)
    st.write("**Большую часть данных составляют низкокачественные варианты (60%), за ними следуют среднекачественные (30%) и высококачественные (10%).**")

    st.header('Вопрос 3')
    st.write("Каковы диапазоны значений для непрерывных переменных 'температура воздуха', 'температура процесса', 'скорость вращения', 'крутящий момент' и 'износ инструмента'? Есть ли выбросы в данных?")
    st.image("reports/q3.png", use_container_width=True)
    st.write("**Скорость вращения может быть выбросом, поэтому на данном этапе мы оставим её в наборе данных.**")

    st.header('Вопрос 4')
    st.write("Есть ли корреляция между непрерывными переменными и меткой 'машинный отказ'? Например, увеличивает ли износ инструмента вероятность отказа машины?")
    st.image("reports/q4.png", use_container_width=True)
    st.write("**Нулевая гипотеза: Нет значимой связи между различными столбцами и отказом машины.**")
    st.write("**Альтернативная гипотеза: Существует значимая связь между износом инструмента и меткой отказа машины.**")
    st.image("reports/h0.png", use_container_width=True)

    st.header('Вопрос 5')
    st.write("Есть ли связь между категориальной переменной 'productID' и непрерывной переменной? Например, выше ли скорость вращения для высококачественных продуктов по сравнению с низкокачественными?")
    st.image("reports/q5.png", use_container_width=True)
    st.write("**Температура процесса, похоже, влияет на машины высокого качества. Следовательно, можно сказать, что температура процесса коррелирует с типом машины.**")

# Оценка производительности
if choice == "Оценка производительности":
    st.title("Модель 1")
    annotated_text(("Лучшая модель 1", "Случайный лес"))
    st.image("reports/model1.png", use_container_width=True)

    st.title("Модель 2")
    annotated_text(("Лучшая модель 2", "Случайный лес"))
    st.image("reports/model2.png", use_container_width=True)

# Отчёты по мониторингу
if choice == "Отчёты по мониторингу":
    options = st.selectbox('Выберите отчёт: ', ('Отчёт по данным', 'Отчёт по модели 1', 'Отчёт по модели 2'))

    if options == 'Отчёт по данным':
        with open("reports/data_drift.html", "r", encoding="utf-8") as f:
            html_report = f.read()
        components.html(html_report, scrolling=True, height=700)

    if options == 'Отчёт по модели 1':
        with open("reports/classification_performance_report.html", "r", encoding="utf-8") as f:
            html_report = f.read()
        components.html(html_report, height=750, scrolling=True)

    if options == 'Отчёт по модели 2':
        with open("reports/classification_performance_report2.html", "r", encoding="utf-8") as f:
            html_report = f.read()
        components.html(html_report, height=750, scrolling=True)

# Прогнозирование
if choice == "Прогнозирование":
    st.title('Прогнозируемое Техническое Обслуживание')
    st.write("**Пожалуйста, введите следующие параметры**")

    # Выпадающий список для типа
    type = st.selectbox('Тип', ('Низкий', 'Средний', 'Высокий'))
    st.write('Вы выбрали:', type)

    # Преобразование типа в числовое значение
    type_mapping = {'Низкий': 0, 'Средний': 1, 'Высокий': 2}
    type_value = type_mapping[type]  # Преобразование в числовое значение

    # Ввод для других параметров
    rpm = st.number_input('RPM', value=0)
    st.write('Текущая скорость вращения (RPM): ', rpm)

    torque = st.number_input('Крутящий момент', value=0)
    st.write('Текущий крутящий момент: ', torque)

    tool_wear = st.number_input('Износ инструмента', value=0)
    st.write('Текущий износ инструмента: ', tool_wear)

    air_temp = st.number_input('Температура воздуха', value=0)
    st.write('Текущая температура воздуха: ', air_temp)

    process_temp = st.number_input('Температура процесса', value=0)
    st.write('Текущая температура процесса: ', process_temp)

    # Кнопка для предсказания
    if st.button("Предсказать"):
        st.write(f"Входные данные: тип={type_value}, rpm={rpm}, torque={torque}, tool_wear={tool_wear}, air_temp={air_temp}, process_temp={process_temp}")
        result1, result2 = prediction(type_value, rpm, torque, tool_wear, air_temp, process_temp)
        st.write(f"Результат предсказания: Отказ машины = {result1}, Тип отказа = {result2}")
        st.write("Отказ машины?: ", result1)
        st.write("Тип отказа: ", result2)


# Функция для скачивания клиента Ollama
def download_ollama():
    ollama_url = "https://ollama.com/download/OllamaSetup.exe"  # Ссылка на клиент Ollama
    response = requests.get(ollama_url, stream=True)

    if response.status_code == 200:
        # Создаем буфер в памяти для файла
        file_buffer = io.BytesIO()
        for chunk in response.iter_content(chunk_size=8192):
            file_buffer.write(chunk)

        # Возвращаем на начало потока
        file_buffer.seek(0)

        # Создаем кнопку для скачивания с предоставлением файла
        st.download_button(
            label="Скачать клиент Ollama",
            data=file_buffer,
            file_name="OllamaSetup.exe",
            mime="application/octet-stream"
        )
        st.success("Клиент доступен для скачивания.")
    else:
        st.error(f"Ошибка при скачивании: {response.status_code}")

# Функция для запуска PowerShell с правами администратора
def run_powershell_as_admin(command):
    try:
        # Запускаем PowerShell с правами администратора и передаем команду для выполнения
        subprocess.run(
            ["powershell", "-Command", f"Start-Process powershell -Verb runAs -ArgumentList '{command}'"],
            check=True
        )
        st.success("Команда успешно выполнена с правами администратора.")
    except Exception as e:
        st.error(f"Ошибка при запуске команды: {str(e)}")

# Функция для отображения информации о модели и её технических требованиях
def display_model_info(model_name):
    global requirements, description
    if model_name == 'Llama 3.3':
        description = """
        **Llama 3.3**: Самая мощная модель с 70B параметрами. Рекомендуется для работы с большими объемами данных.
        - Размер: 43GB
        - Описание: Идеальна для сложных задач, включая генерацию текста и диалоговые системы.
        """
        requirements = """
        - Процессор: 16+ ядер
        - Оперативная память: 64GB+
        - Место на диске: 200GB+
        """
    elif model_name == 'Llama 3.2':
        description = """
        **Llama 3.2**: Отличная модель для большинства задач. Есть две версии: 3B и 1B.
        - Размер: 2.0GB (3B) или 1.3GB (1B)
        - Описание: Подходит для генерации текста и анализа.
        """
        requirements = """
        - Процессор: 8+ ядер
        - Оперативная память: 16GB+
        - Место на диске: 20GB+
        """
    elif model_name == 'Llama 3.1':
        description = """
        **Llama 3.1**: Модель средней мощности с возможностью работы с различными задачами.
        - Размер: 4.7GB (8B) или 231GB (405B)
        - Описание: Хорошо подходит для средних и сложных задач, таких как анализ данных.
        """
        requirements = """
        - Процессор: 12+ ядер
        - Оперативная память: 32GB+
        - Место на диске: 100GB+
        """

    with st.expander(f"Описание модели {model_name}"):
        st.write(description)
        st.write("**Технические требования**")
        st.write(requirements)

# Основная логика Streamlit приложения
def main():
    st.title("Управление моделями GPT на вашем ПК")

    # Выбор модели
    model_choice = st.selectbox(
        'Выберите модель для запуска:',
        ['Llama 3.3', 'Llama 3.2', 'Llama 3.1']
    )

    # Показать описание и технические требования выбранной модели
    display_model_info(model_choice)

    # Определение команды для запуска модели в зависимости от выбора пользователя
    if model_choice == 'Llama 3.3':
        command = 'ollama run llama3.3'
    elif model_choice == 'Llama 3.2':
        command = 'ollama run llama3.2'
    else:
        command = 'ollama run llama3.1'

    # Кнопка для скачивания клиента Ollama
    if st.button("Скачать клиент Ollama"):
        download_ollama()

    # Кнопка для запуска модели
    if st.button(f"Запустить модель {model_choice}"):
        # Выполнение команды через PowerShell с правами администратора
        run_powershell_as_admin(command)

if __name__ == "__main__":
    main()
