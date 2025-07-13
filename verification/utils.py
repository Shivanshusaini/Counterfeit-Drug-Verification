# from supabase import create_client
# import os

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# def upload_qr_to_supabase(filename, file_path):
#     bucket = supabase.storage.from_(SUPABASE_BUCKET)

#     # # Remove if exists
#     # try:
#     #     bucket.remove(filename)
#     # except Exception :
#     #     pass
#     try:
#         bucket.remove(filename)
#         print(f"✅ Old file {filename} removed from Supabase")
#     except Exception as e:
#         print(f"⚠️ Could not remove old file: {e}")

#     # Upload with path
#     bucket.upload(
#         path=filename,
#         file=file_path,
#         file_options={"content-type": "image/png"}  # Ye bahut zaroori hai image dehna ke liya QR ki supabas pe
#     )

#     return bucket.get_public_url(filename)
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_qr_to_supabase(filename, file_path):
    bucket = supabase.storage.from_(SUPABASE_BUCKET)

    print(f"⏳ Overwriting file: {filename} with PUT")

    bucket._upload_or_update(
        method="PUT",
        path=filename,
        file=file_path,
        file_options={"content-type": "image/png"}
    )

    print(f"✅ Overwrite complete")

    return bucket.get_public_url(filename)

