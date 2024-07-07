from notion_mbse.models.document import Document
from notion_mbse.models.document import DocumentSection
from notion_mbse.models.document import DocumentSectionFormatType
from notion_mbse.models.document import DocumentSectionType
from notion_mbse.models.document import DocumentType
from notion_mbse.models.document import FileDocument
from notion_mbse.models.document import FileType
from notion_mbse.models.document import html_to_docsections


def test_document_section():
    section = DocumentSection(
        name="Introduction",
        type=DocumentSectionType.INTRODUCTION,
        sub_type=DocumentSectionFormatType.SECTION,
        section_level=1,
        description="This is the introduction section.",
        document="Example Document",
        section_number=1,
        content="The content of the introduction section.",
        section_length=100,
        references=["Ref1", "Ref2"],
        tags=["intro", "overview"],
        author="John Doe",
        summary="A brief overview of the introduction.",
        related_sections=["Section 2", "Section 3"],
    )

    assert section.name == "Introduction"
    assert section.type == DocumentSectionType.INTRODUCTION
    assert section.sub_type == DocumentSectionFormatType.SECTION
    assert section.section_level == 1
    assert section.description == "This is the introduction section."
    assert section.document == "Example Document"
    assert section.section_number == 1
    assert section.content == "The content of the introduction section."
    assert section.section_length == 100
    assert section.references == ["Ref1", "Ref2"]
    assert section.tags == ["intro", "overview"]
    assert section.author == "John Doe"
    assert section.summary == "A brief overview of the introduction."
    assert section.related_sections == ["Section 2", "Section 3"]
    assert section.section_id == "12345"


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
        type=DocumentType.GENERAL,
        section_ids=["12345", "67890"],
        summary="A brief overview of the example document.",
        keywords=["example", "test"],
        references=["Ref1", "Ref2"],
    )

    assert document.name == "Example Document"


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

    assert file_document.name == "Example File"


def test_document_from_html():
    html_content = """
<html>
<head><title>Example Document</title></head>
<body>
<h1>Introduction</h1>
<p>This is the introduction section.</p>
<h2>Background</h2>
<p>Background information.</p>
<p>More background information.</p>
<h2>Objectives</h2>
<p>Objectives of the document.</p>
<p>Details about objectives.</p>
<h3>Specific Goals</h3>
<p>Details about specific goals.</p>
<ol>
<li>Goal 1</li>
<li>Goal 2</li>
</ol>
</body>
</html>
"""

    document_name = "Example Document"
    sections = html_to_docsections(html_content, document_name)
    for section in sections:
        assert section.document == document_name
        assert section.name in ["Introduction", "Background", "Objectives"]
        assert section.content
        print(section.content)
