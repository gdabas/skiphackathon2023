# Hackathon 2023 - Base app for quick start

This is a Streamlit app for our Hackathon project.

## Setup & Run

1. **Clone the Repository**:

2. **Setup Virtual Environment**:
```
python3 -m venv venv
```


3. **Activate the Virtual Environment**:
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  .\venv\Scripts\activate
  ```

4. **Install Required Packages**:
```
pip install -r requirements.txt
```


**IMPORTANT NOTE**:

create a .env file and add these two line
```
OPENAI_API_KEY = your api key
OPENAI_API_BASE= base Url
```



5. **Run the App**:
```
streamlit run test.py
```


6. **Deactivate the Virtual Environment** (when done):
```
deactivate
```



## Note
Ensure you have Python installed and optionally, a virtual environment tool.
