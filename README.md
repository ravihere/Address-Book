# Address Book API

This is a simple API for an address book application written in Python. It allows users to store and manage their addresses efficiently.

## Features

- Add new addresses with details such as latitude, longitude, and name.
- Update existing addresses.
- Delete addresses.
- Get addresses that are within a given distance and location coordinates.

## Prerequisites

- Python 3.x installed on your system.
- Git

## Installation

1. **Clone the repository** to your local machine:
   
  ```bash
   git clone https://github.com/ravihere/Address-Book.git
  ```

### Alternatively, you can download the repository as a zip file and extract it.

2. Navigate to the project directory:

  ```bash
    cd Address-Book
  ```
  
  3. Create a virtual environment (optional but recommended):
  
  ```bash
    python3 -m venv env
  ```

  4.Activate the virtual environment:
  
  On Windows:
  
  ```bash
  .\env\Scripts\activate
  ```
  
  On macOS and Linux:
  
  ```bash
  source env/bin/activate
  ```

5. Install the required dependencies:
 
    ```bash
    pip install -r requirements.txt
    ```


6. Run the application

    ```bash
    uvicorn main:app --reload
    ```

Uvicorn will start the server, and it will be running on http://127.0.0.1:8000.

7. Check the API documentation:

Open your browser and go to http://127.0.0.1:8000/docs.

  You will see the automatic interactive API documentation provided by Swagger UI.
  You can now use the API endpoints to interact with the address book application.





