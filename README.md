# MQTT Broker Setup Instructions

## Option 1: Install Mosquitto MQTT Broker (Recommended)

### Windows:
1. Download Mosquitto from: https://mosquitto.org/download/
2. Install the software
3. Open Command Prompt as Administrator
4. Navigate to Mosquitto installation directory (usually C:\Program Files\mosquitto)
5. Run: `mosquitto.exe -v`
6. For WebSocket support, create config file `mosquitto.conf`:
```
port 1883
listener 9001
protocol websockets
allow_anonymous true
```
7. Run with config: `mosquitto.exe -c mosquitto.conf -v`

### Alternative: Docker
```bash
docker run -it -p 1883:1883 -p 9001:9001 eclipse-mosquitto
```

## Option 2: Use Online MQTT Broker
- Mosquitto: test.mosquitto.org (port 8000 for WebSocket)
- HiveMQ: broker.hivemq.com (port 8000 for WebSocket)
- Eclipse IoT: iot.eclipse.org (port 80 for WebSocket)

Update the broker URL in both:
1. Jupyter notebook: `MQTT_BROKER = "test.mosquitto.org"`
2. HTML file: Default broker URL input field

## Usage Instructions:

1. **Start MQTT Broker** (if using local Mosquitto)
2. **Run Jupyter Notebook**:
   - Open `pzem_mqtt_simulator.ipynb`
   - Install required packages: `pip install paho-mqtt numpy`
   - Run all cells up to the publishing controls
   - Execute the "start_publishing()" cell to begin data transmission
3. **Open Dashboard**:
   - Open `index.html` in a web browser
   - Configure MQTT broker settings if needed
   - Click "Connect to MQTT" button
   - Watch real-time data on gauges and charts

## Troubleshooting:

- **Connection Failed**: Check if MQTT broker is running and accessible
- **No Data**: Verify topic names match between publisher and subscriber
- **WebSocket Issues**: Ensure broker supports WebSocket protocol on port 9001
- **CORS Issues**: Serve HTML file through a local web server if needed

## MQTT Topics Used:
- `pzem/voltage` - Voltage measurements
- `pzem/current` - Current measurements  
- `pzem/frequency` - Frequency measurements
- `pzem/power_factor` - Power factor measurements
- `pzem/power` - Power measurements
- `pzem/energy` - Energy measurements
- `pzem/all_data` - Combined data payload