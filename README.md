# Kyruus

## Requirements
- The [serverless](https://serverless.com/) framework for deploying the functions and creating required AWS resources.
- [Docker](https://docs.docker.com/v17.09/engine/installation/). The serverless framework uses docker containers to install pypi dependencies, package the lambda and deploy it to AWS. 

## How to deploy this project

NOTE: You can skip this section if you'd just like to use my deployed service (See instructions below).

This repo uses the serverless framework to deploy the project. Please install it first. Link provided above.

- Clone this repo `git@github.com:murali44/Kyruus.git`

- Make sure you have docker running.

- Install the `serverless-python-requirements` plugin. `sls plugin install --name serverless-python-requirements`

- Make sure your AWS account credentials are in the `~/.aws/credentials` file.

- Run `source set_env_vars.sh` to inject environment variables into the Lambda environment.

- Run the deploy command in the repo root folder. `sls deploy -v`

- Note the `GET` endpoint displayed once the service is deployed.

![Endpoint](https://i.imgur.com/oV1yA2C.png "Endpoint")

- Test the service by navigating to the url in a browser.

![browse](https://i.imgur.com/kQaahT5.png "browse")

## What does this API do?

- This is a simple GET API which returns the string `Hello` followed by a name stored in an environment variable. 

- Here's the endpoint I deployed: https://pfw8pdesyf.execute-api.us-east-1.amazonaws.com/dev/helloworld

- The service is currently configured to handle 5 concurrent requests.

## Load testing the API

I'm using [Locust](https://locust.io/) to load test the API.

- Navigate to the `api_test` folder.

- Install the Locust library. `pip install -r requirements.txt`.

- Run the test framework `locust --host=https://pfw8pdesyf.execute-api.us-east-1.amazonaws.com/dev/helloworld`. Update the url if you are using your own deployment.

- Naviagte to `127.0.0.1:8089` in your browser to start load testing. Note: See the cmd line output for the correct port number, it might not be 8089 if you have a service using that port already.

- Set the number of users and spawn rate to send requests to the endpoint.

![test](https://i.imgur.com/0IYfCAr.png "test")

- You should start seeing requests being sent to the endpoint.

![stats](https://i.imgur.com/KBd7XDJ.png "stats")
