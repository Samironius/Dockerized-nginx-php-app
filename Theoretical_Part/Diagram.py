from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.security import WAF
from diagrams.aws.management import Cloudwatch

with Diagram("AWS Architecture", show=False):
    with Cluster("Infrastructure") as infra:
        with Cluster("Frontend"):
            dns = Route53("dns")
            cdn = CloudFront("CDN")
            waf = WAF("WAF")
            elb = ELB("ELB")

        with Cluster("Backend"):
            with Cluster("AutoScaling"):
                svc_group = AutoScaling("AuStoScaling")
                ec2_instances = [EC2(f"EC2_{i} (AZ{i%2+1})") for i in range(3)]
                svc_group >> ec2_instances

            with Cluster("RDS | Multi-AZ"):
                database = [RDS(f"RDS master (AZ1)"), RDS(f"RDS slave (AZ2)")]

            with Cluster("S3 Bucket"):
                storage = S3("S3 Bucket")

        dns >> cdn >> waf >> elb >> svc_group
        for ec2 in ec2_instances:
            for db in database:
                ec2 >> db
            ec2 >> storage

        cloudwatch = Cloudwatch("Cloudwatch")
        cloudwatch - ec2_instances
        cloudwatch - database
        cloudwatch - elb
