import paho.mqtt.client as mqtt
import time
from locust import task, TaskSet, User, between, events
from common import config
from utils.userCount import incrementUser, resetUserCount
import ssl

class MqttTaskSet(TaskSet):
    
    request_count = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.environment = parent.environment

    @task
    def publish_message(self):
        self.request_count += 1
        if self.request_count >= int(config.NUM_REQUESTS):
            self.user.stop()

        self.client.loop_start()
        self.client.start_time = time.monotonic()
        MQTTMessageInfo = self.client.publish(
        self.client._client_id.decode(), self.client.payload, qos=1, retain=False)
        MQTTMessageInfo.wait_for_publish()
        self.client.loop_stop()

    def on_start(self):
        self.client.connect(config.BROKER_HOST, config.BROKER_PORT_TLS, 60)
        self.client.tls_set("/home/joaog/Desensolvimento/pessoal/tcc/analise-mqtt-iot/iot-analise-tcc/locust/certs/ca.crt",
                            tls_version=ssl.PROTOCOL_TLSv1_2)
        self.client.tls_insecure_set(True)
        self.client.subscribe(self.client._client_id.decode())

    def on_stop(self):
        print(f"User {self.client._client_id.decode()} finished with {self.request_count} requests.")
        self.client.disconnect()
        if self.environment.runner.user_count == 1:
            resetUserCount()
            self.user.environment.runner.stop()


class MQTTUserTLS(User):
    tasks = [MqttTaskSet]
    wait_time = between(1, 6)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        devices = incrementUser()
        self.client = mqtt.Client(client_id="devices-{}".format(devices))

        self.client.payload = "012345"
        self.client.start_time = None
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.reached_request_count = False

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    
    def on_publish(self, client, userdata, mid):
        end_time = time.monotonic()
        rtt = end_time - client.start_time
        print("on_publish",rtt)
        events.request.fire(request_type="Round Trip Time", name=client._client_id.decode(), response_time=rtt*1000, response_length=len(client.payload), response="None", 
            context={},
            exception=None,
            start_time=client.start_time,
            url=None,)
        
    def on_message(self, client, userdata, msg):
        end_time = time.monotonic()
        rtt = end_time - client.start_time
        print("on_message",rtt)
        events.request.fire(request_type="latência", name=msg.topic, response_time=rtt*1000, response_length=len(msg.payload), response=None, 
            context={},
            exception=None,
            start_time=client.start_time,
            url=None,)