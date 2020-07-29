from azure_base import AzureBase

from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters


class Storage(AzureBase): 
    def __init__(self, subscription_id, tenant_id, client_id, secret_id): 
        
        super().__init__(
            tenant_id=tenant_id,
            client_id=client_id,
            secret_id=secret_id
        )

        self.subscription_id = subscription_id
        self.Storage_client = StorageManagementClient(
            credentials=self.credentials, 
            subscription_id=subscription_id
        )

    
