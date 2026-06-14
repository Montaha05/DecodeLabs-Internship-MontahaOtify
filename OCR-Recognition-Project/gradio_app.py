import cv2
import gradio as gr
import tempfile

from src.preprocess import preprocess_image
from src.ocr_engine import extract_text_from_image
from src.confindence import (
    calculate_confidence,
    get_status
)
from src.visualize import draw_boxes


def process_uploaded_image(image):

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".jpg",
        delete=False
    )

    image.save(temp_file.name)

    original, gray, blur, processed = preprocess_image(
    temp_file.name
)

    text, data = extract_text_from_image(processed)

    confidence = calculate_confidence(data)

    status = get_status(confidence)

    annotated = draw_boxes(
        original,
        data
    )

    annotated_rgb = cv2.cvtColor(
        annotated,
        cv2.COLOR_BGR2RGB
    )

    return (
        annotated_rgb,
        text,
        f"{confidence:.2f}%",
        status
    )


interface = gr.Interface(
    fn=process_uploaded_image,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Image(label="Annotated Image"),
        gr.Textbox(label="Detected Text"),
        gr.Textbox(label="Confidence"),
        gr.Textbox(label="Status")
    ],
    title="OCR Recognition System",
    description="Upload an image and perform OCR."
)

if __name__ == "__main__":
    interface.launch()