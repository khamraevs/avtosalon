cars = {
    "byd": {
            "model":    "Ford",
            "info":     "Ford Mustang",
            "logo":     "ford_logo",
            "image":    "ford_jpg",
            } 
}

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

marka = "Chevrolet"
model = "Camaro" 
info = "Camaro is bumblebee" 
logo = "camaro_logo" 
image = "camaro image"

add_new_car(cars, marka, 
            model, info, 
            logo, image)

print(cars.keys())