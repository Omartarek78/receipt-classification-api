# Receipt Classification API

- A FastAPI application for receipt classification using a trained model. This API allows users to upload images of receipts and receive predictions on whether the image contains a Handwritten receipt or a receipt or paper, along with confidence levels.

## Features

- Upload images of receipts to be classified by a trained model.
- Get predictions on whether the image contains a Handwritten receipt or a receipt or paper.
- Receive confidence levels for the predictions.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Omartarek78/receipt-classification-api
2. **Navigate to the Project Directory:**

    ```bash
    cd receipt-classification-api
3. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
## Running the API
- To start the FastAPI application, use:
    ```bash
    uvicorn app.main:app --reload
## Example
- You can use curl or any HTTP client to send a request:
   ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/predict' \
    -F 'file=@test/receipt478.jpg'
- A successful response with classification might look like this:
    ```json
    {
    "prediction": 0,
    "confidence level": 0.95
    }
- If the image does not meet the criteria, the response will be:
    ```json
    {
    "prediction": -1
    }
- Classes:

	•	prediction indicates the class: 0 for handwritten receipt, 1 for printed receipt, and 2 for paper.
