from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceAdministrationClient, FaceClient
from azure.ai.vision.face.models import FaceAttributeTypeRecognition04, FaceDetectionModel, FaceRecognitionModel, QualityForRecognition

# Azure Face API credentials
endpoint = 'https://selfie-face.cognitiveservices.azure.com/'
api_key = 'DhGdKb4KkdMaPogeQu0QaGZsizIY2GQmfPnPIMEQnYxHtH9eDcgLJQQJ99AKACfhMk5XJ3w3AAAKACOG7Q65'

# Initialize Face API client
face_client = FaceClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# URL of the image to analyze
image_url = 'https://datanm.blob.core.windows.net/fileupload/image_1.jpg'

# Detect faces in the image
detected_faces = face_client.detect_from_url(
    url=image_url,
    detection_model=FaceDetectionModel.DETECTION03,
    recognition_model=FaceRecognitionModel.RECOGNITION04,
    return_face_id=False,
    return_face_attributes=['age','gender']
)
for face in detected_faces:
    print(f"Face ID: {face.face_id}")
    print(f"Age: {face.face_attributes.age}")
    print(f"Gender: {face.face_attributes.gender}")
    # print(f"Emotions: {face.face_attributes.emotion}")
    # print(f"Head Pose: {face.face_attributes.head_pose}")
print(detected_faces)