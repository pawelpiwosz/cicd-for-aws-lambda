# Demo repository for [Pyconf Hyderabad 2020](https://pyconf.hydpy.org/2020/)

## Introduction

This repository contains whole scenario to follow.  
Some of actions need to be taken separately, some of them might be not described here in full detail.  
In this case, please follow official AWS documentation.

## Github, CodeCommit

To run this tutorial, the repository must be located in CodeCommit. _This_ repository is in Github in order to make it easier to download.  
Of course, the code can be run from Github, CodePipeline has good integration.

## Scenario

Workshop scenario is simple. Small lambda function will be deployed to AWS using AWS CodePipeline using canary deployment.

## Resources

Resources used during this workshop

* Python (to build Lambda function)
* AWS IAM
* AWS CLoudWatch Events
* AWS Lambda
* AWS API Gateway
* AWS CodeCommit
* AWS CodeBuild
* AWS CodeDeploy

## Documentation and all steps

In order to run the lab, please follow the tutorial

1. [Initialization](docs/001_initialization.md)
2. [Repository initialization](docs/002_repository.md)
3. [Setup CodePipeline](docs/003_IaC.md)
