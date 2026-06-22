#!/bin/bash
set -eux

dnf update -y
dnf install -y docker

systemctl enable docker
systemctl start docker

usermod -aG docker ec2-user

cat >/home/ec2-user/README_DEPLOY.txt <<EOF
This instance is prepared for Docker deployments.
GitHub Actions deploys the Flask container using AWS SSM.
EOF