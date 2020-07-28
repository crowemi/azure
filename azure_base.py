from azure.common.credentials import ServicePrincipalCredentials


class AzureBase: 
    def __init__ (self, client_id, secret_id, tenant_id):
        self.credentials = ServicePrincipalCredentials(
            tenant=tenant_id,
            client_id=client_id,
            secret=secret_id
        )

    def get_service_principal_credentials(self):
        return self.credentials        

