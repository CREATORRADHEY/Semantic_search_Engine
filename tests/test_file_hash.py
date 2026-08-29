from utils.file_hash import sha256_file


def test_hash(tmp_path):

    file = tmp_path / "demo.txt"

    file.write_text("hello")

    hash1 = sha256_file(file)
    hash2 = sha256_file(file)

    assert hash1 == hash2