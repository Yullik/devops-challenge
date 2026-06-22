variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "devops-challenge"
}

variable "ssh_cidr" {
  description = "CIDR allowed to SSH to EC2. Replace with your IP/32."
  type        = string
  default     = "1.2.3.4/32"
}