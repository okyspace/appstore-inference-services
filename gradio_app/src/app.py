# import gradio package
import gradio as gr
from config import config
from predict import inputs, outputs, predict

# create gradio interface
demo = gr.Interface(
    fn=predict, 
    inputs=inputs, 
    outputs=outputs,
    examples=config.examples
)

# launch the app
demo.launch(
    share=True
)
