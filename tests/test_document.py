from notion_mbse.models.document import Document
from notion_mbse.models.document import DocumentSection
from notion_mbse.models.document import DocumentSectionFormatType
from notion_mbse.models.document import DocumentSectionType
from notion_mbse.models.document import DocumentType
from notion_mbse.models.document import FileDocument
from notion_mbse.models.document import FileType


def test_document_section():
    section = DocumentSection(
        name="Introduction",
        type=DocumentSectionType.SECTION,
        sub_type=DocumentSectionFormatType.TEXT,
        section_level=1,
        section_description="This is the introduction section.",
        document="Example Document",
        section_number=1,
        content="The content of the introduction section.",
        section_length=100,
        references=["Ref1", "Ref2"],
        tags=["intro", "overview"],
        author="John Doe",
        summary="A brief overview of the introduction.",
        related_sections=["Section 2", "Section 3"],
        section_id="12345",
    )

    print(section.model_dump(mode="json"))


def test_document():
    document = Document(
        name="Example Document",
        description="This is an example document.",
        version="1.0.0",
        tags=["example", "test"],
        sub_type="example",
        created_by="John Doe",
        modified_by="Jane Doe",
        status="active",
        documentation="This is the documentation for the example document.",
        ref_ids=["Ref1", "Ref2"],
        id="12345",
        type=DocumentType.FILE,
        section_ids=["12345", "67890"],
        summary="A brief overview of the example document.",
        keywords=["example", "test"],
        references=["Ref1", "Ref2"],
    )

    print(document.model_dump(mode="json"))


def test_file_document():
    file_document = FileDocument(
        name="Example File",
        description="This is an example file.",
        version="1.0.0",
        tags=["example", "test"],
        sub_type="example",
        created_by="John Doe",
        modified_by="Jane Doe",
        status="active",
        documentation="This is the documentation for the example file.",
        ref_ids=["Ref1", "Ref2"],
        id="12345",
        type=FileType.DOCUMENT,
        section_ids=["12345", "67890"],
        summary="A brief overview of the example file.",
        keywords=["example", "test"],
        references=["Ref1", "Ref2"],
        file_path="/path/to/file",
        file_size=1000,
        file_format="txt",
        file_ext="txt",
    )

    print(file_document.model_dump(mode="json"))