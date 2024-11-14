
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import blob_storage
import json

endpoint = "https://imagetest1genai.cognitiveservices.azure.com/"
key = "3xxzIr4hgeyyNuhmm5K89JD67iuFs5dIhEhiPDYZBhFAvmGgf3M0JQQJ99AKACqBBLyXJ3w3AAALACOGwzdt"
model_id_idcard = "prebuilt-idDocument"



connection_string = "DefaultEndpointsProtocol=https;AccountName=datass;AccountKey=g6HKety2MSSMec+j+k0hISdzHuaTItowvPoAuGeyizfjJpfdMZf22i2CYOQuR2kukHv6Ee/9FDlL+AStTL///Q==;EndpointSuffix=core.windows.net"
container_name = "bank-statement"

# Create BlobServiceClient-- to read from the blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)


blob_name_id = "ID_check.pdf"
file_path_id = r"C:\Users\SRameshwar\Downloads\download.png"
# id_blob_name = blob_storage.read_id(file_path_id,blob_name_id)






# Generate SAS token for the blob
sas_token_id = generate_blob_sas(
    account_name=blob_service_client.account_name,
    container_name=container_name,
    blob_name=blob_name_id,
    account_key="GjyA/D3HuNdmbd2FUJAqD7sGnk3O83Xqnqxed/R6o3WZ4NoGncY7ln+gsC3RinljhCtv6GO0OicM+AStDS1GMA==",  # Alternatively use credentials with the service client
    permission=BlobSasPermissions(read=True),
    expiry=datetime.now() + timedelta(hours=1)  # Token valid for 1 hour
)

# Generate the full URL with the SAS token
formUrl_id = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name_id}?{sas_token_id}"



document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
poller = document_analysis_client.begin_analyze_document_from_url(model_id_idcard, formUrl_id)
result = poller.result()

for idx, document in enumerate(result.documents):
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    print("Document was analyzed by model with ID {}".format(result.model_id))
    key_value= {}
    for name, field in document.fields.items():
        # print(name)
        

        field_value = field.value if field.value else field.content
        key_value[name] = field_value
        # print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
    print(key_value)



### pay_slip_model
model_id_pay_slip = "pay-slip-modelv2"



# connection_string = "DefaultEndpointsProtocol=https;AccountName=datass;AccountKey=g6HKety2MSSMec+j+k0hISdzHuaTItowvPoAuGeyizfjJpfdMZf22i2CYOQuR2kukHv6Ee/9FDlL+AStTL///Q==;EndpointSuffix=core.windows.net"
# container_name = "bank-statement"

# Create BlobServiceClient-- to read from the blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)


blob_name_pay_slip = "payslip-2.pdf"
# file_path_pay_slip = r"C:\Users\SRameshwar\Downloads\payslip\test.pdf"
# id_blob_name = blob_storage.read_pay_slip(file_path_pay_slip,blob_name_pay_slip)






# Generate SAS token for the blob
sas_token_pay_slip = generate_blob_sas(
    account_name=blob_service_client.account_name,
    container_name=container_name,
    blob_name=blob_name_pay_slip,
    account_key="GjyA/D3HuNdmbd2FUJAqD7sGnk3O83Xqnqxed/R6o3WZ4NoGncY7ln+gsC3RinljhCtv6GO0OicM+AStDS1GMA==",  # Alternatively use credentials with the service client
    permission=BlobSasPermissions(read=True),
    expiry=datetime.now() + timedelta(hours=1)  # Token valid for 1 hour
)

# Generate the full URL with the SAS token
formUrl_pay_slip = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name_pay_slip}?{sas_token_pay_slip}"



document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
poller = document_analysis_client.begin_analyze_document_from_url(model_id_pay_slip, formUrl_pay_slip)
result = poller.result()

for idx, document in enumerate(result.documents):
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    print("Document was analyzed by model with ID {}".format(result.model_id))
    # key_value= {}
    for name, field in document.fields.items():
        # print(name)
        

        field_value = field.value if field.value else field.content
        key_value[name] = field_value
        # print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
    print(key_value)





    #### Bank_statement model

    ## pay_slip_model
model_id_bank_stat = "bank_statement_model"



# connection_string = "DefaultEndpointsProtocol=https;AccountName=datass;AccountKey=g6HKety2MSSMec+j+k0hISdzHuaTItowvPoAuGeyizfjJpfdMZf22i2CYOQuR2kukHv6Ee/9FDlL+AStTL///Q==;EndpointSuffix=core.windows.net"
# container_name = "bank-statement"

# Create BlobServiceClient-- to read from the blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)


blob_name_bank_stat = "bank_statement-2.pdf"
# file_path_bank_stat = r"C:\Users\SRameshwar\Downloads\bank_statement\bank_statement-1.pdf"
# id_blob_name = blob_storage.read_bank_statement(file_path_bank_stat,blob_name_bank_stat)






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
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    print("Document was analyzed by model with ID {}".format(result.model_id))
    # key_value= {}
    for name, field in document.fields.items():
        # print(name)
        

        field_value = field.value if field.value else field.content
        key_value[name] = field_value
        # print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
    print(key_value)
    # customer_field = json.dumps(key_value)
    # blob_storage.customer_info(customer_field,"customer_info.json")

        


