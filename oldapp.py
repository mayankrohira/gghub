from flask import Flask, request, render_template, jsonify, redirect, url_for
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'  # Directory where uploaded files will be saved
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Set up Azure Form Recognizer client
endpoint = "https://imagetest1genai.cognitiveservices.azure.com/"
key = "3xxzIr4hgeyyNuhmm5K89JD67iuFs5dIhEhiPDYZBhFAvmGgf3M0JQQJ99AKACqBBLyXJ3w3AAALACOGwzdt"
credential = AzureKeyCredential(key)
client = DocumentAnalysisClient(endpoint=endpoint, credential=credential)

# Index route (HTML form for uploading documents)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return jsonify({"message": f"File uploaded successfully: {filename}"}), 200
    else:
        return jsonify({"error": "File type not allowed"}), 400



# Route to handle document upload and analysis
@app.route('/analyze', methods=['POST'])
def analyze_document():
    # Check if the post request has a file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    # Ensure a file was uploaded
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Send file to Form Recognizer (via DocumentAnalysisClient)
        poller = client.begin_analyze_document("prebuilt-document", file.stream)
        result = poller.result()

        # Extract data from the result
        data = []
        for page in result.pages:
            page_data = {
                "page_number": page.page_number,
                "lines": [{"text": line.content} for line in page.lines]
            }
            data.append(page_data)

        return render_template('result.html', data=data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(port=8000)