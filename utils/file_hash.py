from pathlib import Path
import hashlib


def sha256_file(path: str | Path) -> str:
    """
    Returns SHA256 checksum for a file.
    """

    sha = hashlib.sha256()

    with open(path, "rb") as file:

        while chunk := file.read(8192):
            sha.update(chunk)

    return sha.hexdigest()