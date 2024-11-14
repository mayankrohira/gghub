from flask import Flask, request, render_template, jsonify, redirect, url_for
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
import blob_storage
import json
from model_run import Document_analysis
# Initialize Flask app
app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'  # Directory where uploaded files will be saved
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
endpoint = "https://imagetest1genai.cognitiveservices.azure.com/"
key = "3xxzIr4hgeyyNuhmm5K89JD67iuFs5dIhEhiPDYZBhFAvmGgf3M0JQQJ99AKACqBBLyXJ3w3AAALACOGwzdt"
global connection_string
global container_name 
global file_id 
global file_pay_slip
global file_bank_statement


connection_string="DefaultEndpointsProtocol=https;AccountName=datass;AccountKey=g6HKety2MSSMec+j+k0hISdzHuaTItowvPoAuGeyizfjJpfdMZf22i2CYOQuR2kukHv6Ee/9FDlL+AStTL///Q==;EndpointSuffix=core.windows.net"

container_name= "bank-statement"

# Create BlobServiceClient-- to read from the blob
global blob_service_client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
headers = {
    "Content-Type": "application/json"
}

# Function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Index route (HTML form for uploading documents)
@app.route('/')
def index():
    return 1

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if file and allowed_file(file.filename):
#         filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filename)
#         return jsonify({"message": f"File uploaded successfully: {filename}"}), 200
#     else:
#         return jsonify({"error": "File type not allowed"}), 400



# Route to handle document upload and analysis
@app.route('/analyze', methods=['POST'])
def analyze_document():
    # Check if the post request has a file part

    
    file_id = request.json['file_id']
    file_pay_slip=request.json['file_pay_slip']
    file_bank_statement=request.json['file_bank_statement']


    try:

        return Document_analysis(blob_service_client,container_name,file_id,file_pay_slip,file_bank_statement),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(port=3000)