import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None
__area_type = None

def get_estimated_price(location, sqft, bhk, bath, area_type):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    try:
        area_index = __data_columns.index(area_type.lower())
    except:
        area_index = -1

    x = np.zeros(len(__data_columns))
    if loc_index >= 0:
        x[loc_index] = 1
    if area_index >= 0:
        x[area_index] = 1
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations
def get_area_names():
    return __area_type

def load_saved_artifacts():
    print("loading saved artifacts.... start")
    global __data_columns
    global __locations
    global  __area_type
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:242]
        __area_type = __data_columns[242:245]
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Artifacts loaded successfully")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_area_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 'built-up area'))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 'Plot  Area'))
    # print(get_estimated_price('Boka', 1000, 2, 2, 'Ploea'))
    # print(get_estimated_price('Boka', 1000, 2, 2, 'Ploea'))