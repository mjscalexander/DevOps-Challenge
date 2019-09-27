import json
import requests
import time
import logging
import statistics
# My logger that will be sent to stdout
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler_info = logging.FileHandler('hello_healthcheck.log', mode='w')
file_handler_info.setFormatter(formatter)
logger.addHandler(file_handler_info)


def healthchecker():
    url = "http://10.10.0.2:80/health"
    latency = []
    # sends a request to the above url in a while loop
    while True:
        response = requests.get(url=url).json()
        healthcheck = json.loads(response)
        latency.append(healthcheck["latency"])
        time.sleep(10)
        if healthcheck["healthy"] == False:
            logger.critical("hello service unhealthy due to high latency")
        # when latency list gathers 6 elements (60 secs.) is logs the below info and clears the list to start all over again
        if len(latency) == 6:
            logger.info('best: {} , worst: {}, avg: {}'.format(min(latency), max(latency), statistics.mean(latency)))
            latency.clear()



if __name__ == "__main__":
    time.sleep(5)
    logger.info("health checker starting...")
    print(healthchecker())



