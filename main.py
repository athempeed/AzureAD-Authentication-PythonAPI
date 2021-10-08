from fastapi import FastAPI,Security
import appConfig 
from api import api_router
from fastapi_azure_auth.auth import SingleTenantAzureAuthorizationCodeBearer


app = app = FastAPI(
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': appConfig.CLIENT_ID
    },
)

azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=appConfig.CLIENT_ID,
    tenant_id=appConfig.TENANT_ID,
    scopes={
         f'api://{appConfig.CLIENT_ID}/User-Read': 'User-Read',
    }
)


app.include_router(api_router, prefix="/api",dependencies=[Security(azure_scheme, scopes=['User-Read'])])
