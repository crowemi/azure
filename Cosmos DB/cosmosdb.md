# Azure Cosmos DB

## Data Distribution and Partitions (DP200)

## Consistancy Model (DP200)

- Strong (stronger consistency) Reads are guaranteed to return the most recent committed version of an item.
- Bounded Staleness
  - n-versions or T-time
  - all records within n-seconds/minutes must be fresh
  - top n-records must be fresh
- Session
  - create a session for each user, read your own writes
- Consistent Prefix
  - You can be guarenteed read order and write order
- Eventual (weaker consistency)
  - Data will eventually update

## Concepts and APIs (DP200)

- SQL API (core)
- Gremlin API (graph)
- MongoDB API (document)
- Table API (table)
- Cassandra API (columnar based)

## Multiple Master Replication

**only works in premium-tier

### [az cosmostdb create](https://docs.microsoft.com/en-us/cli/azure/cosmosdb?view=azure-cli-latest#az-cosmosdb-create)

    az cosmosdb create 
        --name (required)
        --resource-group (required)
        --location (optional)
        --kind (optional, 
            values {
                GlobalDocumentDB,
                MongoDB,
                Parse
            } 
        )
        --default-consistency-level
        --locations (optional,
            values {
                regionName=(string),
                failoverPriority=(int),
                isZoneRedundant=(bool)
            }
        )
        --enable-multiple-write-locations
