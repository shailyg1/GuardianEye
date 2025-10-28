from PIL import Image
import imagehash
import json
import os

DATASET_PATH = 'data/media_hashes.json'

def scan_image(image_file):
    image = Image.open(image_file)
    img_hash = str(imagehash.phash(image))
    # Load hash dataset
    if os.path.exists(DATASET_PATH):
        with open(DATASET_PATH, "r") as f:
            hash_db = json.load(f)
    else:
        hash_db = {}
    # Check for duplicates (threshold 5 for similar images)
    for img_name, stored_hash in hash_db.items():
        if imagehash.hex_to_hash(stored_hash) - imagehash.hex_to_hash(img_hash) < 5:
            return f"Possible leaked/similar image found: {img_name}"
    # Add new hash to db
    hash_db[image_file.name] = img_hash
    with open(DATASET_PATH, "w") as f:
        json.dump(hash_db, f)
    return "No leak detected. Image added to database."
