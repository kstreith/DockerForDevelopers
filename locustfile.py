from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")
        
    @task
    def talks(self):
        self.client.get("/talks/")

    @task
    def gab2017(self):
        self.client.get("/articles/gab2017/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
