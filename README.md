Packet Sniffer Dashboard
A cloud-based network packet sniffer with a web dashboard, deployed on Google Cloud Platform.

Project Overview
This project demonstrates a network packet sniffer with a web-based dashboard, designed for educational purposes and network analysis practice. It captures packets from various external sources and displays them in a user-friendly web interface, leveraging Google Cloud Platform for deployment and data storage.

This is a demo version using mock data

Transitioning to Real GCP Integration
To use this project with real Google Cloud Platform integration:

Set up a GCP project and enable necessary APIs (Firestore, Cloud Run)
Create a service account with appropriate permissions
Download the service account key JSON file
Modify the app.py file to use Firestore instead of mock data
Update the Dockerfile to include your service account key
Never commit your service account key to public repositories
For detailed instructions on GCP setup, refer to the official Google Cloud documentation.

Features
Captures network packets from multiple sources:
Public test server (test.rebex.net)
DNS queries
Public API (JSONPlaceholder)
Stores captured packet data in Google Cloud Firestore
Provides a web interface to view and filter captured packets
Deployable to Google Cloud Platform (GCP) using Cloud Run
Continuous deployment using GitHub Actions
Prerequisites
Python 3.9+
Google Cloud Platform account
Docker
Git
Project Structure
packet-sniffer-dashboard/ │ ├── .github/ │ └── workflows/ │ └── deploy.yml │ ├── templates/ │ └── index.html │ ├── app.py ├── packet_sniffer.py ├── requirements.txt ├── Dockerfile ├── README.md └── .gitignore Copy

Setup and Installation
Clone the repository: git clone https://github.com/your-username/packet-sniffer-dashboard.git cd packet-sniffer-dashboard Copy
Install dependencies: pip install -r requirements.txt Copy
Set up GCP:
Create a new project in Google Cloud Console
Enable Firestore, Cloud Run, and Container Registry APIs
Create a service account with Firestore access and download the JSON key
Set environment variable for GCP authentication: export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-key.json" Copy
Running the Packet Sniffer Locally
Start the packet sniffer: sudo python packet_sniffer.py Copy
Generate sample traffic: ftp test.rebex.net nslookup example.com curl https://jsonplaceholder.typicode.com/posts/1 Copy
Deployment to GCP
Build the Docker image: docker build -t gcr.io/[YOUR_PROJECT_ID]/packet-sniffer-dashboard . Copy
Push the image to Google Container Registry: docker push gcr.io/[YOUR_PROJECT_ID]/packet-sniffer-dashboard Copy
Deploy to Cloud Run: gcloud run deploy packet-sniffer-dashboard --image gcr.io/[YOUR_PROJECT_ID]/packet-sniffer-dashboard --platform managed --allow-unauthenticated --region us-central1 Copy
CI/CD with GitHub Actions
This project uses GitHub Actions for continuous deployment. To set it up:

Fork this repository
In your forked repository, go to Settings > Secrets
Add the following secrets:
GCP_PROJECT_ID: Your Google Cloud project ID
GCP_SA_KEY: The content of your service account JSON key
Push changes to the main branch to trigger automatic deployment
Usage
After deployment, access the web dashboard through the URL provided by Cloud Run. Use the buttons to filter packets by source and view the captured network traffic.

Security and Ethical Considerations
Only use this tool on networks you own or have explicit permission to monitor
Be aware of privacy laws and regulations in your area
Do not capture or store sensitive information
Use this tool responsibly and ethically
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see details.

Acknowledgments
Scapy library for packet manipulation
Flask for the web framework
Google Cloud Platform for hosting and storage