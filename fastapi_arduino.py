#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware
import csv
#from random import randrange
from pydantic import BaseModel


#header = ['temp',  'distance']

class DataTempDistance(BaseModel):
    temperature: float
    humidity: float

class button1(BaseModel):
    on: int




app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
    "*",
    "179.12.150.177",
    
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
app = FastAPI(title="Arduino FastAPI",
              description="Here's our API...", version="1.0")


@app.post('/api/arduino/', summary="", description="")
async def arduino(request: DataTempDistance):
    with open('arduino_data.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        #print(request)
        data = [request.temperature, request.humidity]
        print(data)
        writer.writerow(data)
    print("Arduino")
    pass


@app.get("/api/arduino/", tags=["todos"])
async def get_temperatureerature():
    with open('arduino_data.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        line_count = 0
        data_object = []

        for row in csv_reader:
            if line_count == 0:
                print(f'las columnas actuales son {", ".join(row)}')
                line_count += 1
            else:
                data_object.append(DataTempDistance(temperature=row[0],humidity=row[1]))
                line_count += 1
    print(f'Processed {line_count} lines')

    return {"body": data_object}





#Get y Post de button 1

@app.post('/api/arduino/button1', summary="", description="")
async def postbutton1(request: button1):
    with open('arduino_databutton1.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/button1", tags=["todos"])
async def get_button1():
    with open('arduino_databutton1.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}


# Get y Post Button 2
@app.post('/api/arduino/button2', summary="", description="")
async def postbutton2(request: button1):
    with open('arduino_databutton2.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )


@app.get("/api/arduino/button2", tags=["todos"])
async def get_button2():
    with open('arduino_databutton2.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}

# Get y Post Button 3
@app.post('/api/arduino/button3', summary="", description="")
async def postbutton3(request: button1):
    with open('arduino_databutton3.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/button3", tags=["todos"])
async def get_button3():
    with open('arduino_databutton3.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}


# Get y Post Button 4
@app.post('/api/arduino/button4', summary="", description="")
async def postbutton4(request: button1):
    with open('arduino_databutton4.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/button4", tags=["todos"])
async def get_button4():
    with open('arduino_databutton4.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}

# Get y Post Button 2
@app.post('/api/arduino/button5', summary="", description="")
async def postbutton5(request: button1):
    with open('arduino_databutton5.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/button5", tags=["todos"])
async def get_button5():
    with open('arduino_databutton5.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}

# Get y Post Button 6
@app.post('/api/arduino/button6', summary="", description="")
async def postbutton6(request: button1):
    with open('arduino_databutton6.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/button6", tags=["todos"])
async def get_button6():
    with open('arduino_databutton6.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}

# Turn First 3 off
@app.get("/api/arduino/turnoff", tags=["todos"])
async def turnbuttonsoff():
    with open('arduino_databutton1.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = ["False"]
        print(data)
        writer.writerow(data)
    print("Arduino")


    with open('arduino_databutton2.csv', 'w', encoding='UTF8') as f:
        writer2 = csv.writer(f)
        # write the data
        # print(request)
        data = ["False"]
        print(data)
        writer2.writerow(data)
    print("Arduino")

    with open('arduino_databutton3.csv', 'w', encoding='UTF8') as f:
        writer3 = csv.writer(f)
        # write the data
        # print(request)
        data = ["False"]
        print(data)
        writer3.writerow(data)
    print("Arduino")

    return (f"Botones cambiado a False" )


# Turn First 3 off
@app.get("/api/arduino/turnoff1", tags=["todos"])
async def turnbuttonsoff():
    with open('arduino_databutton4.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = ["False"]
        print(data)
        writer.writerow(data)
    print("Arduino")


    with open('arduino_databutton5.csv', 'w', encoding='UTF8') as f:
        writer2 = csv.writer(f)
        # write the data
        # print(request)
        data = ["False"]
        print(data)
        writer2.writerow(data)
    print("Arduino")

    with open('arduino_databutton6.csv', 'w', encoding='UTF8') as f:
        writer3 = csv.writer(f)
        # write the data
        # print(request)
        data = ["False"]
        print(data)
        writer3.writerow(data)
    print("Arduino")

    return (f"Botones cambiado a False" )




    







#Get y Post Garage
@app.post('/api/arduino/garage', summary="", description="")
async def arduino(request: button1):
    with open('arduino_datagarage.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/garage", tags=["todos"])
async def get_garage():
    with open('arduino_datagarage.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}
















#Get y post alerta
@app.post('/api/arduino/alerta', summary="", description="")
async def arduino(request: button1):
    with open('arduino_dataalerta.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        # print(request)
        data = [request.on]
        print(data)
        writer.writerow(data)
    print("Arduino")

    return (f"Button cambiado a {request.on}" )
    pass

@app.get("/api/arduino/alerta", tags=["todos"])
async def get_alerta():
    with open('arduino_dataalerta.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        data_object = []
        row1 = next(csv_reader)
        print(row1)
        #ta_object.append(button1(on=row1))
    return {"on": row1}





if __name__ == "__main__":

    uvicorn.run("fastapi_arduino:app", host="127.0.0.1",
                port=5000, log_level="info", debug=True)
