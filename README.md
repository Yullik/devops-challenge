# DevOps Technical Challenge

## Overview

This project deploys a containerized Flask application to AWS using Terraform for Infrastructure as Code and GitHub Actions for CI/CD.

The application exposes a single endpoint:

`/info`

which returns:

* EC2 Instance ID
* Availability Zone
* Current Timestamp

## Architecture

GitHub Actions → Amazon ECR → AWS Systems Manager (SSM) → EC2 (Docker) → Application Load Balancer

## Infrastructure

Terraform provisions:

* EC2 t3.micro instance
* Application Load Balancer
* Target Group and Listener
* Security Groups
* Amazon ECR Repository
* IAM Role and Instance Profile
* SSM access for deployments

Security controls include:

* ALB exposed on port 80
* Application port 5000 accessible only from the ALB
* SSH restricted to a single IP address
* EC2 IAM role with minimal permissions required for ECR and SSM
* IMDSv2 enabled

## Deployment

### Infrastructure

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### CI/CD

The GitHub Actions workflow:

1. Builds the Docker image
2. Pushes the image to Amazon ECR
3. Deploys the container to EC2 using AWS SSM

The workflow runs automatically on pushes to the main branch and can also be triggered manually from GitHub Actions.

## AWS Credentials

AWS credentials are not stored in code.

Terraform uses AWS credentials supplied through the AWS CLI configuration.

GitHub Actions uses the following repository secrets:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

## Assumptions

* AWS region: us-east-1
* Default VPC and subnets are available
* Single EC2 instance is sufficient for the challenge
* Docker container listens on port 5000
* Deployment uses AWS SSM rather than SSH

## Production Improvements

Given additional time, I would implement:

* HTTPS with ACM certificates
* Auto Scaling Group
* Private subnets
* Remote Terraform state (S3 + DynamoDB)
* CloudWatch logging and monitoring
* Blue/green deployments
* WAF protection
* More granular IAM permissions
* Automated post-deployment smoke tests
