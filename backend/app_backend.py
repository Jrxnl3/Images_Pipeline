from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil

app = FastAPI(title="Image Upload API", description="Upload images including RAW files", version="1.0")

UPLOAD_DIR = Path("/app/upload")
BACKUP_DIR = Path("/app/backup")

UPLOAD_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

@app.post("/upload", summary="Upload an image file", tags=["Upload"])
async def upload_image(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    file_path = UPLOAD_DIR / file.filename
    backup_path = BACKUP_DIR / file.filename

    try:
        with file_path.open("wb") as buffer:
            buffer.write(await file.read())

        shutil.copy2(file_path, backup_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")

    return JSONResponse({
        "filename": file.filename,
        "message": f"Image uploaded successfully to {UPLOAD_DIR} and backed up to {BACKUP_DIR}"
    })
