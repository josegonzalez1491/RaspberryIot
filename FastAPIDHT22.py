# Librerías a instalar
# pip install fastapi uvicorn[standard] pymodbus==3.11.4

# librerías
import asyncio # para usar el comando delay
from pymodbus.client import ModbusTcpClient # protoclo modbus
from fastapi import FastAPI, WebSocket #Para montar el servidor
from fastapi.responses import HTMLResponse #Respuesta de parte del serVidor
#Datos para la conexion
IP = "192.168.2.101"
PORT = 502

#Definición de registros
REG_TEMP = 0
REG_HUM = 1

app = FastAPI()

HTML = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8"/>
    <title>Monitoreo DHT22</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #333;
        }

        .container {
            text-align: center;
        }

        h2 {
            color: #fff;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }

        .card {
            background: #ffffff;
            padding: 25px 30px;
            border-radius: 16px;
            width: 320px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        .value {
            font-size: 1.6rem;
            margin: 15px 0;
            padding: 12px;
            border-radius: 10px;
            transition: transform 0.2s ease;
        }

        .value:hover {
            transform: scale(1.03);
        }

        .temp {
            background: #ffe5e5;
            color: #c0392b;
        }

        .hum {
            background: #e6f4ff;
            color: #2980b9;
        }

        .label {
            font-size: 0.9rem;
            opacity: 0.8;
        }

        .number {
            font-size: 2.2rem;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌡️ Monitoreo DHT22</h2>
        <div class="card">
            <div id="temp" class="value temp">
                <div class="label">Temperatura</div>
                <div class="number">-- °C</div>
            </div>
            <div id="hum" class="value hum">
                <div class="label">Humedad</div>
                <div class="number">-- %</div>
            </div>
        </div>
    </div>

    <script>
        let ws = new WebSocket("ws://" + location.host + "/ws");

        ws.onmessage = function(event){
            let data = JSON.parse(event.data);

            document.querySelector("#temp .number").innerHTML =
                data.temp.toFixed(2) + " °C";

            document.querySelector("#hum .number").innerHTML =
                data.hum.toFixed(2) + " %";
        };
    </script>
</body>
</html>
"""


@app.get("/")
def home():
    return HTMLResponse(HTML)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    client = ModbusTcpClient(IP, port=PORT)

    if not client.connect():
        print("Conexion con el ESP32 no establecida")
        await ws.send_json({"temp": 0, "hum": 0})
        await ws.close()
        return

    print("Conexión establecida. Leyendo cada 5 segundos \n")

    try:
        while True:
            rr = client.read_holding_registers(REG_TEMP, count=2, device_id=1)

            if rr.isError():
                print("Error en la lectura")
            else:
                temp = rr.registers[0]
                hum = rr.registers[1]
                print(f"Temperatura: {temp/100.0:.2f} | Humedad: {hum/100.0:.2f}")
                await ws.send_json({"temp": temp/100.0, "hum":hum/100.0})
            await asyncio.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        await ws.close()
        print("Conexción cerrada")
        print("Programa finalizado")