
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import blob_storage
import json

endpoint = "https://imagetest1genai.cognitiveservices.azure.com/"
key = "3xxzIr4hgeyyNuhmm5K89JD67iuFs5dIhEhiPDYZBhFAvmGgf3M0JQQJ99AKACqBBLyXJ3w3AAALACOGwzdt"




connection_string = "DefaultEndpointsProtocol=https;AccountName=datass;AccountKey=g6HKety2MSSMec+j+k0hISdzHuaTItowvPoAuGeyizfjJpfdMZf22i2CYOQuR2kukHv6Ee/9FDlL+AStTL///Q==;EndpointSuffix=core.windows.net"
container_name = "bank-statement"

# Create BlobServiceClient-- to read from the blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def Document_analysis(blob_service_client,container_name,file_id,file_pay_slip,file_bank_statement):

    blob_name_id = file_id 
    blob_name_pay_slip = file_pay_slip
    blob_name_bank_stat = file_bank_statement

    model_id_idcard = "prebuilt-idDocument"
    model_id_pay_slip = "pay-slip-modelv2"
    ## pay_slip_model
    model_id_bank_stat = "bank_statement_model"


# Generate SAS token for the blob
    sas_token_id = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=blob_name_id,
        account_key="GjyA/D3HuNdmbd2FUJAqD7sGnk3O83Xqnqxed/R6o3WZ4NoGncY7ln+gsC3RinljhCtv6GO0OicM+AStDS1GMA==",  # Alternatively use credentials with the service client
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now() + timedelta(hours=1)  # Token valid for 1 hour
    )
    formUrl_id = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name_id}?{sas_token_id}"
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Make sure your document's type is included in the list of document types the custom model can analyze
    poller = document_analysis_client.begin_analyze_document_from_url(model_id_idcard, formUrl_id)
    result = poller.result()

    for idx, document in enumerate(result.documents):

        key_value= {}
        for name, field in document.fields.items():
            # print(name)
            

            field_value = field.value if field.value else field.content
            key_value[name] = field_value
            # print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
        # print(key_value)



    # Generate SAS token for the blob
    sas_token_pay_slip = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=blob_name_pay_slip,
        account_key="GjyA/D3HuNdmbd2FUJAqD7sGnk3O83Xqnqxed/R6o3WZ4NoGncY7ln+gsC3RinljhCtv6GO0OicM+AStDS1GMA==",  # Alternatively use credentials with the service client
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now() + timedelta(hours=1)  # Token valid for 1 hour
    )

    
    formUrl_pay_slip = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name_pay_slip}?{sas_token_pay_slip}"

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Make sure your document's type is included in the list of document types the custom model can analyze
    poller = document_analysis_client.begin_analyze_document_from_url(model_id_pay_slip, formUrl_pay_slip)
    result = poller.result()

    for idx, document in enumerate(result.documents):

        for name, field in document.fields.items():
            # print(name)
            

            field_value = field.value if field.value else field.content
            key_value[name] = field_value
            # print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
        # print(key_value)



    # Generate SAS token for the blob
    sas_token_bank_statement = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=blob_name_bank_stat,
        account_key="GjyA/D3HuNdmbd2FUJAqD7sGnk3O83Xqnqxed/R6o3WZ4NoGncY7ln+gsC3RinljhCtv6GO0OicM+AStDS1GMA==",  # Alternatively use credentials with the service client
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now() + timedelta(hours=1)  # Token valid for 1 hour
    )

    # Generate the full URL with the SAS token
    
    formUrl_bank_stat = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name_bank_stat}?{sas_token_bank_statement}"

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Make sure your document's type is included in the list of document types the custom model can analyze
    poller = document_analysis_client.begin_analyze_document_from_url(model_id_bank_stat, formUrl_bank_stat)
    result = poller.result()

    for idx, document in enumerate(result.documents):

        # key_value= {}
        for name, field in document.fields.items():
            # print(name)
            

            field_value = field.value if field.value else field.content
            key_value[name] = field_value
            # print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
    return(key_value)
        
            


# print(Document_analysis(blob_service_client,container_name,file_id,file_pay_slip,file_bank_statement))