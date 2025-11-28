"""
MQTT Connection Test Script
This script tests the MQTT broker connectivity before running the main simulation.
"""

import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Successfully connected to MQTT broker!")
        print("Connection result code:", rc)
        
        # Test publishing a message
        test_message = {
            "test": True,
            "timestamp": time.time(),
            "message": "MQTT connection test successful"
        }
        
        result = client.publish("pzem/test", json.dumps(test_message))
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print("✅ Test message published successfully!")
        else:
            print("❌ Failed to publish test message")
    else:
        print(f"❌ Failed to connect to MQTT broker. Return code: {rc}")
        print("Return code meanings:")
        print("0: Connection successful")
        print("1: Connection refused - incorrect protocol version")
        print("2: Connection refused - invalid client identifier")
        print("3: Connection refused - server unavailable")
        print("4: Connection refused - bad username or password")
        print("5: Connection refused - not authorised")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published")

def test_mqtt_connection(broker_host="test.mosquitto.org", port=1883):
    """Test MQTT broker connection"""
    
    print("🧪 Testing MQTT Connection...")
    print(f"Broker: {broker_host}:{port}")
    print("-" * 40)
    
    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    
    try:
        # Attempt connection
        print(f"Attempting to connect to {broker_host}:{port}...")
        client.connect(broker_host, port, 60)
        
        # Start network loop
        client.loop_start()
        
        # Wait for connection
        time.sleep(3)
        
        # Stop loop and disconnect
        client.loop_stop()
        client.disconnect()
        
        print("-" * 40)
        print("🏁 Connection test completed!")
        
    except Exception as e:
        print(f"❌ Connection error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure MQTT broker (Mosquitto) is running")
        print("2. Check if the broker address and port are correct")
        print("3. Verify firewall settings")
        print("4. Try using a public broker like 'broker.hivemq.com'")

if __name__ == "__main__":
    # Test with test.mosquitto.org (default)
    print("Testing test.mosquitto.org MQTT broker...")
    test_mqtt_connection("test.mosquitto.org", 1883)
    
    print("\n" + "="*50 + "\n")
    
    # Test with local broker
    print("Testing local MQTT broker...")
    test_mqtt_connection("localhost", 1883)