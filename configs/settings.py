from pathlib import Path
import os

class project_dir():

    PROJECT_DIR = Path(__file__).parent.parent.absolute()

    DATA_DIR = PROJECT_DIR/'data'

    RAW_DATA_DIR = DATA_DIR/'raw'

    CLEANED_DIR = DATA_DIR/'cleaned'


