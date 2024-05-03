from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def calculate_avg_age(self):
        self.client.get("test/avg_age/")
