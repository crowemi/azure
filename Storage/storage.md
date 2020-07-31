# Azure Storage

How to classify your data?  
How your data will be used?  
How to get the best performance for your application?  

Azure  SQL Database - Structured (Relational)  
Azure Cosmos DB - Structured, semi-structured (serialization language), unstructured

* Document DB
* Key Value stores
* Column family stores
* Graph Database

---

## Data Serialization Language

* XML
* JSON
* YAML

## NoSQL

* Key value - store data in key value pairs
* Graph - nodes that contain records that point to other nodes
* Document - store markup language JSON, XML

---
Operations an latency  
Ask yourself these questions:

* Will you be doing simple lookups using an ID?
* Do you need to query the database for one or more fields?
* How many create, update, and delete operations do you expect?
* Do you need to run complex analytical queries?
* How quickly do these operations need to complete?

Let’s walk through each of the data sets with these questions in mind and discuss the requirements.

ACID Guarantees

* Atomicity means a transaction must execute exactly once and must be atomic; either all of the work is done, or none of it is. Operations within a transaction usually share a common intent and are interdependent.

* Consistency ensures that the data is consistent both before and after the transaction.

* Isolation ensures that one transaction is not impacted by another transaction.

* Durability means that the changes made due to the transaction are permanently saved in the system. Committed data is saved by the system so that even in the event of a failure and system restart, the data is available in its correct state.

Storage account is a container that groups a set of Auzre Storage service together.

Storage account defines policy that applies to all storage services in the account.

## Subscription

## Location

## Performance

## Replication

### Single Region Replication

* LRS - Locally redundant storage, three copies single availability zone. (default; three copies of data stored locally)
* ZRS - Zone redundant storage, syncronously replicates data within the primary region across three availabilty zones.

### Multiple Region Replication

* GRS - Geo-redundant storage uses LRS in primary region syncronously and copies data to secondary region using LRS asyncronously.
* RA-GRS - Read access geo-redundant storage; same as GRS but allows read access to secondary region.
* GZRS - Geo-redundant storage uses ZRS in primary region syncronously and copies data to seconary region asyncronously.
* RA-GZRS - Read access geo-redundant storage; same as GZRS but allows read access to secondary region.

## Access tier

* How quickly you can access data (hot, cold)

## Secure transfer required

* Supported protocols for accessing data HTTP/S

## Virtual networks

* Allows inbound access requests only from virtual networks specified

You need one storage account for every group of settings to apply

## Data diversity

* Specific to country or region?
* Public and private data?  

## Cost sensitivity

## Tolerance for management overhead

A typical strategy is to start with an analysis of your data and create partitions that share characteristics like location, billing, and replication strategy, and then create one storage account for each partition.


## Provision Non-Relational Data Store (DP200) 

Create storage account:

    az storage account create 
        --name (required)
        --resource-group (required)
        --location (optional)
        --sku ( optional, 
                values {
                    Premium_LRS, 
                    Premium_ZRS, 
                    Standard_GRS, 
                    Standard_GZRS, 
                    Standard_LRS, 
                    Standard_RAGRS, 
                    Standard_RAGZRS, 
                    Standard_ZRS
                }
            )
        --kind (optional,
                values { 
                    BlobStorage, 
                    BlockBlobStorage, 
                    FileStorage, 
                    Storage, 
                    StorageV2
                }
            )

Delete storage account:

    az storage account delete
        --name (optional)
        --resource-group (optional)
