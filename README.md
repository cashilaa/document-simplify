This project extracts unstructured data from complex documents and converts it into structured data. It uses asyncflows to create an asynchronous workflow for processing the documents.

Development Environment Setup:

Clone the GitHub repository.
git clone https://github.com/cashilaa/document-simplify.git
Create a virtual environment:

python -m venv venv
Activate the virtual environment:
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the necessary dependencies:

pip install gradio asyncflows aiofiles PyMuPDF

Running the Project:

Run the main application:
python main.py

Open the provided URL in your browser to access the Gradio interface.
Flow and Custom Action:

Flow: The flow is defined in flow.py and includes actions added to it.
Custom Action: The ExtractStructuredDataAction in actions.py processes the extracted text and converts it into structured data.
Use Cases:

Extracting structured data from research papers.
Extracting key information from contracts.
Converting report content into a structured format for further analysis.
