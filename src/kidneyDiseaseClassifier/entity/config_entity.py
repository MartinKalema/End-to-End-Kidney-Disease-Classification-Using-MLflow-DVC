from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for data ingestion process.

    Attributes:
        root_dir (Path): The root directory where data will be stored or processed.
        source_URL (str): The URL from which data will be fetched.
        local_data_file (Path): The local file path where the downloaded data will be stored.
        unzip_dir (Path): The directory where the downloaded data will be extracted or unzipped.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """Configuration class for preparing base models.
    
    Attributes:
        root_dir (Path): The root directory where model-related files are stored.
        base_model_path (Path): The path where the base model will be saved.
        updated_base_model_path (Path): The path where the updated base model will be saved.
        params_image_size (list): A list representing the image size parameters.
        params_learning_rate (float): The learning rate parameter.
        params_include_top (bool): Whether to include the top layer in the model.
        params_weights (str): The weights to be used in the model.
        params_classes (int): The number of classes in the model.
    """
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int