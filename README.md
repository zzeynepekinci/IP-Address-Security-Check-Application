# IP-Address-Security-Check-Application

## Project Description  
This application is designed to check the security status of IP addresses. It determines whether an IP address is involved in suspicious activities and informs the user if it is safe or potentially dangerous. The application performs threat analysis using an API to check if an IP address is blacklisted.

## Features  
- Check the security status of IP addresses  
- Detect whether an IP address is involved in suspicious activities  
- Retrieve information about malicious IPs  
- Provide a user-friendly interface for security assessments  

## Technologies Used  
- **Python** – Core programming language of the application  
- **Flask** – Web framework used for development  
- **Requests** – Used for making HTTP requests  
- **AbuseIPDB API** – Used to retrieve security data of IP addresses  
- **HTML/CSS** – Used for a simple user interface  

## Installation  

Before proceeding, ensure that **Python 3.x** is installed on your system. Follow these steps to set up the application:

1. Clone the repository:  
   ```bash
   git clone https://github.com/username/repository-name.git
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:  
   ```bash
   python app.py
   ```

4. Open your browser and go to:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage  
Once the application is running, the main page will display a field where you can enter an IP address. You will receive instant feedback on whether the entered IP address is safe or associated with malicious activities. If the IP is flagged as dangerous, the application will issue a warning.  
