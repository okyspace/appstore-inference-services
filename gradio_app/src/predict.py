import gradio as gr
from config import config
from utils import load_model
from utils import read_data
from utils import infer

inputs = [
    gr.Image(
        source="upload",
        type="filepath",
        label="image for inference",
        show_label=True,
        shape=(200, 200)
    ),
    "text",
    gr.Slider(0, 100)
]
outputs = [
    gr.Image(
        type="filepath",
        label="inference result",
        show_label=True,
        shape=(200, 200)
    ),
    "text",
    gr.Slider(),

]

# setup
model = load_model()
# TODO load others

def predict(imagepath, text, scale):
    data = read_data(imagepath)
    return imagepath, text, scale
