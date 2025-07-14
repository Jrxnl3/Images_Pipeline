import time
from pathlib import Path
from dotenv import load_dotenv

from Strategy.BlackAndWhiteStratey import BlackAndWhiteProcessing
from logger import log

global processing_strategy

def watch_folder():
    processed_files = set()

    log.info(f"Watching folder {UPLOAD_DIR} for new images...")
    while True:
        for file_path in UPLOAD_DIR.iterdir():
            if file_path.is_file() and file_path.name not in processed_files:
                process_image(file_path)
                processed_files.add(file_path.name)
        time.sleep(5)

def process_image(file_path: Path):
    log.info("Processing: %s", file_path.name)
    try:
        time.sleep(1)
        processing_strategy.process(file_path, PROCESSED_DIR)
        log.info("Processed: %s", file_path.name)
    except Exception as e:
        log.error("Failed to process %s", file_path.name, exc_info=True)


if __name__ == '__main__':
    load_dotenv()

    UPLOAD_DIR = Path("/app/uploads")
    PROCESSED_DIR = Path("/app/processed")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    log.info("Starting logging!")

    processing_strategy = BlackAndWhiteProcessing()

    watch_folder()