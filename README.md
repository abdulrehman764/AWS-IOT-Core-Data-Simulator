# AWS-IOT-Core-Data-Simulator

This Python script is designed to simulate the generation and transmission of solar energy data to an IoT topic using AWS IoT Core. It generates random data related to solar power generation and sends it to an AWS IoT topic at regular intervals.

## Configuration
Before running the script, you need to configure the following parameters in the code:

- `iot_client`: The AWS IoT client used to publish messages to AWS IoT Core.
- `topic`: The name of the IoT topic to which the simulated data will be published.

## Script Overview

### 1. Data Generation
The script generates random solar energy-related data, including DCPower, ACPower, SunlightIntensity, DailyYield, temperature, city, masterid, and state. This data is generated in batches, with each batch containing 200 records.

### 2. Data Publication
The generated data is formatted into a string and published to the specified IoT topic using the AWS IoT client. The script sends 10 batches of data, with a 1-second pause between each batch.

## How to Run

1. Ensure you have the required AWS credentials and the AWS IoT client configured.
2. Modify the configuration parameters at the beginning of the script, such as the `iot_client` and `topic`, to match your IoT setup.
3. Execute the script, and it will simulate the generation and transmission of solar energy data to the specified IoT topic.

## Note

- This script is designed for simulation and testing purposes. Ensure that you have the necessary permissions and IoT Core setup in AWS for message publication.
- The generated data is entirely random and does not reflect actual solar energy readings.
- Be mindful of potential costs associated with data transmission and storage in AWS IoT Core when using this script for testing.

Feel free to reach out if you have any questions or need further assistance.
