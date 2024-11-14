from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Set up the connection to Azure Blob Storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=datass;AccountKey=g6HKety2MSSMec+j+k0hISdzHuaTItowvPoAuGeyizfjJpfdMZf22i2CYOQuR2kukHv6Ee/9FDlL+AStTL///Q==;EndpointSuffix=core.windows.net"
container_name = "bank-statement"

def read_id (file_path,blob_name):
    # blob_name = "ID_check.pdf"
    # file_path = r"C:\Users\SRameshwar\Downloads\bank_statement\bank_statement-3.pdf"
    # file_path = f"{file_path}"
    # file_path = r

    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the file
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"File {file_path} uploaded to {container_name}/{blob_name}")



def read_pay_slip (file_path,blob_name):
    # blob_name = "pay_slip_check.pdf"
    # file_path = r"C:\Users\SRameshwar\Downloads\bank_statement\bank_statement-3.pdf"

    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the file
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"File {file_path} uploaded to {container_name}/{blob_name}")




def read_bank_statement (file_path,blob_name):
    # blob_name = "bank_statement_check.pdf"
    # file_path = r"C:\Users\SRameshwar\Downloads\bank_statement\bank_statement-3.pdf"

    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the file
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"File {file_path} uploaded to {container_name}/{blob_name}")


def customer_info (file,blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Step 3: Get the container client
    container_client = blob_service_client.get_container_client(container_name)

    # Step 4: Upload the JSON string to Azure Blob Storage
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the JSON string to the blob as a stream
    blob_client.upload_blob(file, overwrite=True)

    print(f"Successfully uploaded {blob_name} to container {container_name}.")



