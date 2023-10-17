from typing import Optional, Literal
from pydantic import BaseSettings, Field

class Config(BaseSettings):
    """Define any config here.

    See here for documentation:
    https://pydantic-docs.helpmanual.io/usage/settings/
    """
    source: str = "upload"
    model_weights: str = Field(default="/app/models/model.pt", description="Path to model weights", env="MODEL_WEIGHTS")
    device: str = Field(default="cpu", description="Device to use for inference", env="DEVICE")
    classes_csv: str = Field(default="/app/configs/classes.csv", description="")
    outputs: str = Field(default="/app/outputs", description="Path to tmp output inference results", 
    examples: List[str] = [
        "/app/examples/bird.jpg"
    ]
config = Config()
