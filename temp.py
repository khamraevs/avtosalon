cars = {
    "byd": {
            "model":    "arrizo",
            "info":     "arrizo Mustang",
            "logo":     "arrizo_logo",
            "image":    "arrizo_jpg",
            },
    "ford": {
            "model":    "Ford",
            "info":     "Ford Mustang",
            "logo":     "ford_logo",
            "image":    "ford_jpg",
            }, 
}

# # 1 metod
# del cars["ford"]
# print(cars)

# # 2 metod
def delete_car(dict_car, car_name):
    car = dict_car.pop(car_name)
    return car

a = delete_car(cars, "ford")
print(a)