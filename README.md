# Resume Enhancement and Customization Tool (REACT)

## REACT Description
A tool that leverages a specified Large Language Model (LLM) to enhance a user's resume based on information that is stored in Firestore.
After a user provides their relevant resume information and details (does not need to be an resume format and language), the user would then chat with a bot and typically start with providing the job description a user has in mind. The REACT tool would then recreate the user's resume based on all of the information provided without overselling the user for skills they do not have.

## How to Install and Run the Project
1. Run UV and sync the project.
2. Create a secrets.toml file that has the following

Google Authentication
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "XXX"
client_id = "XXX"
client_secret = "XXX"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

[GOOGLE_APPLICATION_CREDENTIALS]
type = "service_account"
project_id = "insert-project-id"
private_key_id = "XXX"
private_key = "-----BEGIN PRIVATE KEY-----\XXX\n-----END PRIVATE KEY-----\n"
client_email = "XXX.iam.gserviceaccount.com"
client_id = "XXX"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/xxxx/firebase-adminsdk-xxx%40XXXX.iam.gserviceaccount.com"
universe_domain = "googleapis.com"

[llm_keys]
openai_key = "XXX"
google_gemini_key = "XXX"

[langsmith]
api_key = "XXX"
tracing = "true"
endpoint = "https://api.smith.langchain.com"
project = "XXX"