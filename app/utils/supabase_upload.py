from supabase import create_client
import uuid
from fastapi import HTTPException, UploadFile
import os
from dotenv import load_dotenv
from storage3.exceptions import StorageException  # <- not StorageExceptions

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET_NAME = "avatars"

def upload_image_to_supabase(file: UploadFile, user_id: str) -> str:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        file_ext = file.filename.split(".")[-1]
        file_id = f"{user_id}_{uuid.uuid4()}.{file_ext}"

        file_content = file.file.read()

        supabase.storage.from_(BUCKET_NAME).upload(
            path=file_id,
            file=file_content,
            file_options={"content-type": file.content_type}
        )

        return f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/{file_id}"

    except StorageException as e:
        raise HTTPException(status_code = 500, detail = f"Upload failed: {str(e)}")