from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def index(self):
        self.client.get("/")
        #https://pfw8pdesyf.execute-api.us-east-1.amazonaws.com/dev/helloworld

class WebsiteUser(HttpLocust):
    task_set = UserBehavior