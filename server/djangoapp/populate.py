from .models import CarMake, CarModel

def initiate():
    # --- Car Make Data ---
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"}, # Index 0
        {"name":"Mercedes", "description":"Great cars. German technology"}, # Index 1
        {"name":"Audi", "description":"Great cars. German technology"}, # Index 2
        {"name":"Kia", "description":"Great cars. Korean technology"}, # Index 3
        {"name":"Toyota", "description":"Great cars. Japanese technology"}, # Index 4
        # --- New Makes Added ---
        {"name":"Ford", "description":"American muscle and trucks. Built Ford Tough."}, # Index 5
        {"name":"Honda", "description":"Reliable and efficient. Japanese engineering."}, # Index 6
        {"name":"BMW", "description": "Sheer Driving Pleasure. German engineering."} # Index 7
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # --- Car Model Data ---
    # Note: Added 'dealer_id' to each entry
    car_model_data = [
      # Nissan (Index 0)
      {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
      {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
      {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1},
      {"name":"Sentra", "type":"Sedan", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 2},
      
      # Mercedes (Index 1) - Corrected types
      {"name":"A-Class", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 1},
      {"name":"C-Class", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 1},
      {"name":"E-Class", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 1},
      {"name":"GLE", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2},

      # Audi (Index 2) - Corrected types
      {"name":"A4", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3},
      {"name":"A5", "type":"COUPE", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3},
      {"name":"A6", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3},
      {"name":"Q5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 4},

      # Kia (Index 3) - Corrected types
      {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 5},
      {"name":"Carnival", "type":"VAN", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 5},
      {"name":"Cerato", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 6},
      {"name":"Telluride", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 6},

      # Toyota (Index 4)
      {"name":"Corolla", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 7},
      {"name":"Camry", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 7},
      {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 8},
      {"name":"RAV4", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 8},

      # --- New Models Added ---
      
      # Ford (Index 5)
      {"name":"F-150", "type":"TRUCK", "year": 2023, "car_make":car_make_instances[5], "dealer_id": 9},
      {"name":"Mustang", "type":"COUPE", "year": 2023, "car_make":car_make_instances[5], "dealer_id": 9},
      {"name":"Explorer", "type":"SUV", "year": 2023, "car_make":car_make_instances[5], "dealer_id": 10},

      # Honda (Index 6)
      {"name":"Civic", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[6], "dealer_id": 11},
      {"name":"Accord", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[6], "dealer_id": 11},
      {"name":"CR-V", "type":"SUV", "year": 2023, "car_make":car_make_instances[6], "dealer_id": 12},

      # BMW (Index 7)
      {"name":"3 Series", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[7], "dealer_id": 13},
      {"name":"X3", "type":"SUV", "year": 2023, "car_make":car_make_instances[7], "dealer_id": 14},
      {"name":"X5", "type":"SUV", "year": 2023, "car_make":car_make_instances[7], "dealer_id": 14},
    ]

    # Updated creation loop to include dealer_id
    for data in car_model_data:
            CarModel.objects.create(
                name=data['name'], 
                car_make=data['car_make'], 
                type=data['type'], 
                year=data['year'],
                dealer_id=data['dealer_id']
            )