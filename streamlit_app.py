
import streamlit as st
import requests

# Заголовок приложения
st.title('Недвижимость: предсказание цен')
# Вывод изображения с внешнего URL
st.image('https://advantagefinancesa.com.au/wp-content/uploads/2017/04/Investing-in-property-doesnt-have-to-cost-you-millions-_717_6053220_0_14102411_1000.jpg')

st.write('Это приложение предсказывает цену на недвижимость на основании признаков ниже')
st.write(
    'Сразу хочу предупредить что первые 12 признаков оказывают больший вес на предсказание',
    'Остальные признаки мы добавили для лучшей обобщающей способности модели',
    'Без них предсказание ухудшается, заполнять их необязательно',
    "Ещё вот надо отметить что если вы укажете просто 1 какой-нибудь признак",
    'Например площадь, а ванные например оставите около 0 и тд., будет не совсем корректное предсказание',
    'Согласитесь очень странно что недвижимость с максимальной площадью не имеет ванных комнат или спален'
    
)


# Создание интерфейса для ввода данных
sqft = st.slider('Площадь(в квадратных футах)')
beds = st.slider('Спальни')
stories = st.slider('Количество этажей')
num_baths = st.slider('Количество ванных комнат')
additional_bath = st.slider('Дополнительные ванные комнаты')
school_r_mean = st.slider('Средний рейтинг школы')
school_dist = st.slider('Расстояние до школы (мили)')
year_built = st.number_input('Год постройки')
heating = st.slider('Отопление', 0, 1, 0)
cooling = st.slider('Охлаждение', 0, 1, 0)
parking = st.slider('Парковка', 0, 1, 0)
lotsize = st.slider('Площадь участка (в квадратных футах)')
status_0 = st.slider('Статус 0', 0, 1, 0)
status_1 = st.slider('Статус 1', 0, 1, 0)
status_2 = st.slider('Статус 2', 0, 1, 0)
status_3 = st.slider('Статус 3', 0, 1, 0)
propertyType_0 = st.slider('Тип недвижимости 0', 0, 1, 0)
propertyType_1 = st.slider('Тип недвижимости 1', 0, 1, 0)
propertyType_2 = st.slider('Тип недвижимости 2', 0, 1, 0)
city_0 = st.slider('Город 0', 0, 1, 0)
city_1 = st.slider('Город 1', 0, 1, 0)
city_2 = st.slider('Город 2', 0, 1, 0)
city_3 = st.slider('Город 3', 0, 1, 0)
city_4 = st.slider('Город 4', 0, 1, 0)
city_5 = st.slider('Город 5', 0, 1, 0)
city_6 = st.slider('Город 6', 0, 1, 0)
zipcode_0 = st.slider('Почтовый индекс 0', 0, 1, 0)
zipcode_1 = st.slider('Почтовый индекс 1', 0, 1, 0)
zipcode_2 = st.slider('Почтовый индекс 2', 0, 1, 0)
zipcode_3 = st.slider('Почтовый индекс 3', 0, 1, 0)
zipcode_4 = st.slider('Почтовый индекс 4', 0, 1, 0)
zipcode_5 = st.slider('Почтовый индекс 5', 0, 1, 0)
zipcode_6 = st.slider('Почтовый индекс 6', 0, 1, 0)
zipcode_7 = st.slider('Почтовый индекс 7', 0, 1, 0)
zipcode_8 = st.slider('Почтовый индекс 8', 0, 1, 0)
zipcode_9 = st.slider('Почтовый индекс 9', 0, 1, 0)
zipcode_10 = st.slider('Почтовый индекс 10', 0, 1, 0)
zipcode_11 = st.slider('Почтовый индекс 11', 0, 1, 0)
zipcode_12 = st.slider('Почтовый индекс 12', 0, 1, 0)
state_0 = st.slider('Штат 0', 0, 1, 0)
state_1 = st.slider('Штат 1', 0, 1, 0)
state_2 = st.slider('Штат 2', 0, 1, 0)
state_3 = st.slider('Штат 3', 0, 1, 0)
state_4 = st.slider('Штат 4', 0, 1, 0)
state_5 = st.slider('Штат 5', 0, 1, 0)
MlsId_0 = st.slider('MlsId 0', 0, 1, 0)
MlsId_1 = st.slider('MlsId 1', 0, 1, 0)
MlsId_2 = st.slider('MlsId 2', 0, 1, 0)
MlsId_3 = st.slider('MlsId 3', 0, 1, 0)
MlsId_4 = st.slider('MlsId 4', 0, 1, 0)
MlsId_5 = st.slider('MlsId 5', 0, 1, 0)
MlsId_6 = st.slider('MlsId 6', 0, 1, 0)
MlsId_7 = st.slider('MlsId 7', 0, 1, 0)
MlsId_8 = st.slider('MlsId 8', 0, 1, 0)
MlsId_9 = st.slider('MlsId 9', 0, 1, 0)
MlsId_10 = st.slider('MlsId 10', 0, 1, 0)
MlsId_11 = st.slider('MlsId 11', 0, 1, 0)
MlsId_12 = st.slider('MlsId 12', 0, 1, 0)
MlsId_13 = st.slider('MlsId 13', 0, 1, 0)
MlsId_14 = st.slider('MlsId 14', 0, 1, 0)
MlsId_15 = st.slider('MlsId 15', 0, 1, 0)
MlsId_16 = st.slider('MlsId 16', 0, 1, 0)
MlsId_17 = st.slider('MlsId 17', 0, 1, 0)
school_types_0 = st.slider('Типы школ 0', 0, 1, 0)
school_types_1 = st.slider('Типы школ 1', 0, 1, 0)
school_types_2 = st.slider('Типы школ 2', 0, 1, 0)
street_type_0 = st.slider('Тип улицы 0', 0, 1, 0)
street_type_1 = st.slider('Тип улицы 1', 0, 1, 0)
street_type_2 = st.slider('Тип улицы 2', 0, 1, 0)
street_type_3 = st.slider('Тип улицы 3', 0, 1, 0)
street_zone_0 = st.slider('Зона улицы 0', 0, 1, 0)
street_zone_1 = st.slider('Зона улицы 1', 0, 1, 0)
street_zone_2 = st.slider('Зона улицы 2', 0, 1, 0)

# Кнопка для отправки данных на сервер FastAPI и получения предсказания
if st.button('Предсказать цену'):
    # Формирование данных для отправки
    data = {
        "sqft": sqft,
        "beds": beds,
        "stories": stories,
        "num_baths": num_baths,
        "additional_bath": additional_bath,
        "school_r_mean": school_r_mean,
        "school_dist": school_dist,
        "year_built": year_built,
        "heating": heating,
        "cooling": cooling,
        "parking": parking,
        "lotsize": lotsize,
        "status_0": status_0,
        "status_1": status_1,
        "status_2": status_2,
        "status_3": status_3,
        "propertyType_0": propertyType_0,
        "propertyType_1": propertyType_1,
        "propertyType_2": propertyType_2,
        "city_0": city_0,
        "city_1": city_1,
        "city_2": city_2,
        "city_3": city_3,
        "city_4": city_4,
        "city_5": city_5,
        "city_6": city_6,
        "zipcode_0": zipcode_0,
        "zipcode_1": zipcode_1,
        "zipcode_2": zipcode_2,
        "zipcode_3": zipcode_3,
        "zipcode_4": zipcode_4,
        "zipcode_5": zipcode_5,
        "zipcode_6": zipcode_6,
        "zipcode_7": zipcode_7,
        "zipcode_8": zipcode_8,
        "zipcode_9": zipcode_9,
        "zipcode_10": zipcode_10,
        "zipcode_11": zipcode_11,
        "zipcode_12": zipcode_12,
        "state_0": state_0,
        "state_1": state_1,
        "state_2": state_2,
        "state_3": state_3,
        "state_4": state_4,
        "state_5": state_5,
        "MlsId_0": MlsId_0,
        "MlsId_1": MlsId_1,
        "MlsId_2": MlsId_2,
        "MlsId_3": MlsId_3,
        "MlsId_4": MlsId_4,
        "MlsId_5": MlsId_5,
        "MlsId_6": MlsId_6,
        "MlsId_7": MlsId_7,
        "MlsId_8": MlsId_8,
        "MlsId_9": MlsId_9,
        "MlsId_10": MlsId_10,
        "MlsId_11": MlsId_11,
        "MlsId_12": MlsId_12,
        "MlsId_13": MlsId_13,
        "MlsId_14": MlsId_14,
        "MlsId_15": MlsId_15,
        "MlsId_16": MlsId_16,
        "MlsId_17": MlsId_17,
        "school_types_0": school_types_0,
        "school_types_1": school_types_1,
        "school_types_2": school_types_2,
        "street_type_0": street_type_0,
        "street_type_1": street_type_1,
        "street_type_2": street_type_2,
        "street_type_3": street_type_3,
        "street_zone_0": street_zone_0,
        "street_zone_1": street_zone_1,
        "street_zone_2": street_zone_2
    }
    
    # Отправка POST-запроса на сервер FastAPI
    # верный response = requests.post("http://127.0.0.1:8000/predict/", json=data)
    #response = requests.post("http://host.docker.internal:8000/predict/", json=data)
    
    #fastapi_url = "http://my-streamlit-app:8000/predict/"

    #fastapi_url = "http://0.0.0.0:8000/predict/"
    #fastapi_url = "http://my-streamlit-app:8000/predict/"
    fastapi_url = "http://localhost:8000/predict/" # рабочий варик 
    #fastapi_url = "http://server:8501/predict/"

    response = requests.post(fastapi_url, json=data)
    # Обработка ответа
    if response.status_code == 200:
        result = response.json()
        predicted_price = result["predicted_price"]
        st.success(f'Предсказанная цена: ${predicted_price:.2f}')
    else:
        st.error('Ошибка при получении предсказания. Пожалуйста, попробуйте снова.')


