def add_new_car(cars, marka, 
                model, info, 
                logo, image):
    new_car = {marka: {
                "model":    model,
                "info":     info,
                "logo":     logo,
                "image":    image
                }} 
    cars.update(new_car)
    return "All done"

def delete_car(dict_car, car_name):
    car = dict_car.pop(car_name)
    return car