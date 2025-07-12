from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_qr_to_supabase(filename, file_path):
    bucket = supabase.storage.from_(SUPABASE_BUCKET)

    # Remove if exists
    try:
        bucket.remove(filename)
    except Exception:
        pass

    # Upload with path
    bucket.upload(
        path=filename,
        file=file_path,
        file_options={"content-type": "image/png"}  # Ye bahut zaroori hai
    )

    return bucket.get_public_url(filename)


