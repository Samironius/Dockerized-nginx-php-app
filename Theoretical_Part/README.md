# Simplified AWS Architecture

This repository showcases a simplified AWS architecture using Diagrams as Code. It illustrates the infrastructure setup with frontend and backend components, highlighting key AWS services.

## Architecture Overview

The architecture consists of the following components:

- **Frontend Cluster**: Contains services responsible for handling frontend functionality.

- **Backend Cluster**: Includes services responsible for backend processing.

- **AutoScaling**: Represents the Auto Scaling group for dynamic scaling of EC2 instances.

- **RDS | Multi-AZ**: Represents the multi-Availability Zone configuration for the RDS database.

- **S3 Bucket**: Represents the storage bucket for data storage.

- **Route53 ("dns")**: Amazon Route 53 for DNS management.

- **CloudFront ("CDN")**: Amazon CloudFront for content delivery acceleration.

- **WAF ("WAF")**: AWS WAF for web application firewall protection.

- **ELB ("ELB")**: Elastic Load Balancing for distributing incoming traffic.

- **CloudWatch ("Cloudwatch")**: Amazon CloudWatch for monitoring performance metrics.


## Achieving the Goals

**High Availability**: High Availability is achieved by utilizing multiple Availability Zones in AWS. For example, EC2 instances can be distributed across different Availability Zones, ensuring continuity of operation even if one zone becomes unavailable. Additionally, RDS is configured with Multi-AZ, providing automatic database recovery in case of failure.

**Fault Tolerance**: Fault Tolerance is achieved through the use of services that automatically recover from failures. For instance, if one of the EC2 instances fails, Auto Scaling automatically replaces it with a new instance. Similarly, using Multi-AZ for RDS ensures automatic database recovery in case of failure.

**Disaster Recovery**: Disaster Recovery is achieved through data backup and recovery in case of a catastrophe. For example, S3 can be used to store backup copies of data that can be restored if needed.

**Auto Scaling**: Auto Scaling is achieved through AWS Auto Scaling, which automatically adjusts the number of EC2 instances based on incoming traffic.

**Enhanced security**: Enhanced security is achieved by utilizing AWS WAF to protect web applications from security threats and by using IAM to manage access to AWS resources.