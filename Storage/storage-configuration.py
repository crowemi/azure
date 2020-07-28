import os

from azure.mgmt.resource import SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials



from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters


subscription_id = ''

credentials = ServicePrincipalCredentials(
    tenant='',
    client_id='',
    secret=''
)


client = ResourceManagementClient(credentials, subscription_id)
resource_groups = client.resource_groups.list()

for item in client.resource_groups.list():
    print(item)

# for item in resource_client.resource_groups.list(): 
#     print(item)

# storage_client = StorageManagementClient(credentials, subscription_id)

# resource_group_params = {'location':'westus'}

# for sa in storage_client.storage_accounts.list():
#     print(sa)
