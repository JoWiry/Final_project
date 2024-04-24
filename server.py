
# добавить признаки в графу всякие разные  и проверить 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Загрузка десериализованной модели
pipeline_from_joblib = joblib.load('final_model_pipeline.joblib')

# Определение структуры данных для входных параметров
class InputData(BaseModel):
    sqft: int
    beds: int
    stories: float
    num_baths: int
    additional_bath: float
    school_r_mean: float
    school_dist: float
    year_built: int
    heating: int
    cooling: int
    parking: int
    lotsize: float
    status_0: int
    status_1: int
    status_2: int
    status_3: int
    propertyType_0: int
    propertyType_1: int
    propertyType_2: int
    city_0: int
    city_1: int
    city_2: int
    city_3: int
    city_4: int
    city_5: int
    city_6: int
    zipcode_0: int
    zipcode_1: int
    zipcode_2: int
    zipcode_3: int
    zipcode_4: int
    zipcode_5: int
    zipcode_6: int
    zipcode_7: int
    zipcode_8: int
    zipcode_9: int
    zipcode_10: int
    zipcode_11: int
    zipcode_12: int
    state_0: int
    state_1: int
    state_2: int
    state_3: int
    state_4: int
    state_5: int
    MlsId_0: int
    MlsId_1: int
    MlsId_2: int
    MlsId_3: int
    MlsId_4: int
    MlsId_5: int
    MlsId_6: int
    MlsId_7: int
    MlsId_8: int
    MlsId_9: int
    MlsId_10: int
    MlsId_11: int
    MlsId_12: int
    MlsId_13: int
    MlsId_14: int
    MlsId_15: int
    MlsId_16: int
    MlsId_17: int
    school_types_0: int
    school_types_1: int
    school_types_2: int
    street_type_0: int
    street_type_1: int
    street_type_2: int
    street_type_3: int
    street_zone_0: int
    street_zone_1: int
    street_zone_2: int

# Создание экземпляра FastAPI
app = FastAPI()

# Определение маршрута и метода для получения прогноза
@app.post("/predict/")
async def predict_price(data: InputData):
    try:
        # Преобразование входных данных в массив numpy
        input_features = np.array(list(data.model_dump().values())).reshape(1, -1)        
        # Предсказание цены с использованием загруженной модели
        predicted_price = pipeline_from_joblib.predict(input_features)
        
        # Возврат предсказанной цены
        return {"predicted_price": predicted_price[0]}
    
    except Exception as e:
        # Если возникла ошибка, возвращаем сообщение об ошибке
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8000) 
    uvicorn.run(app, host="0.0.0.0", port=8000)
