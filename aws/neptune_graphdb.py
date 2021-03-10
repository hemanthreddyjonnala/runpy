'''
Amazon Neptune makes it easy to set up, operate, and scale a graph database in the cloud. 
Before launching Neptune databases, you need to configure a DB Subnet Group.

Subnets are segments of a VPC's IP address range that allow you to group your resources based on security and operational needs. A DB Subnet Group is a collection of subnets (typically private) that you create in a VPC and designate for your DB instances. Each DB subnet group should have subnets in at least two Availability Zones in a given region.

When creating a DB in a VPC, you must select a DB subnet group. Amazon Neptune uses that DB subnet group and your preferred Availability Zone to select a subnet and an IP address within that subnet to associate with your DB instance. When Amazon Neptune creates a DB in a VPC, it assigns a network interface to your DB instance by using an IP address selected from your DB Subnet Group. If the primary DB instance of a Multi-AZ deployment fails, Amazon Neptune can promote the corresponding standby and subsequently create a new standby using an IP address from an assigned subnet in one of the other Availability Zones.

You can create an RDS Subnet Group using the RDS launch wizard.
'''

ENDPOINT=https://neptune-cluster.cluster-cmjknsthci7l.us-west-2.neptune.amazonaws.com:8182/sparql

SPARQL command to insert a singleton in the graph database:
curl -X POST --data-binary 'update=INSERT DATA { <https://example.com/subject> <https://example.com/predicate> <https://example.com/object> . }' $ENDPOINT

 retrieve the triple you just created, enter the following SPARQL command:
 curl -X POST --data-binary 'query=select ?subject ?predicate ?object where {?subject ?predicate ?object} limit 3' $ENDPOINT
