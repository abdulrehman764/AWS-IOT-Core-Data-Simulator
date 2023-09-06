import boto3
import time
import json
import random

iot_client = boto3.client('iot-data')
topic = 'solar_data_test'

def send_message():
    for _ in range(10): 
        payload_rows = []
        print("Sending message", _)
        for _ in range(200):
            DCPower = random.randint(500, 1000)
            ACPower = random.randint(500, 1000)
            SunlightIntensity = random.randint(1000, 5000)
            DailyYield = random.randint(90000, 110000)
            temperature = random.randint(80, 120)
            city = random.choice(["H", "S", "D", "A", "F", "E", "A", "C", "P", "L", "Z"])
            masterid = random.randint(1, 10)
            state = "Texas"
            row = f"{DCPower},{ACPower},{SunlightIntensity},{DailyYield},{temperature},{state},{city},{masterid}"
            
            payload_rows.append(row)
    
        payload = ';'.join(payload_rows)  # Join rows with newline
        print(payload)
        print(type(payload))
        #payload += ';' 
        # payload = bytes(payload, 'utf-8')
        # payload = json.dumps(payload)
        response = iot_client.publish(topic=topic, qos=1, payload=payload)
        response = iot_client.publish(topic=topic, qos=1, payload=payload)
        response = iot_client.publish(topic=topic, qos=1, payload=payload)
        response = iot_client.publish(topic=topic, qos=1, payload=payload)
        response = iot_client.publish(topic=topic, qos=1, payload=payload)
        response = iot_client.publish(topic=topic, qos=1, payload=payload)
        time.sleep(1)  # Pause for 1 second between messages

def lambda_handler(event, context):
    # TODO implement
    send_message()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
