from models.document import Document


def test_document_creation():

    document = Document(

        filename="demo.pdf",

        source="pdf",

        text="Hello AI"

    )

    assert document.filename == "demo.pdf"

    assert document.source == "pdf"

    assert document.text == "Hello AI"