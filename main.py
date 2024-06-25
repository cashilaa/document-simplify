from actions import ExtractStructuredDataAction
from utils import extract_text_from_pdf
from flow import Flow
import gradio as gr

async def extract_structured_data(input_pdf):
    try:
        text = await extract_text_from_pdf(input_pdf.name)
        structured_data = await flow.execute_action('extract_structured_data', text)
        return structured_data
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize flow and add actions
flow = Flow()
flow.add_action('extract_structured_data', ExtractStructuredDataAction())

# Define Gradio interface
iface = gr.Interface(
    fn=extract_structured_data,
    inputs=[
        gr.File(label="Upload Document (PDF)")
    ],
    outputs="json",
    title="Structured Data Extractor",
    description="Upload a document to extract structured data."
)

# Launch the interface
iface.launch()
