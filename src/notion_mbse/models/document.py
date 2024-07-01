#!/usr/bin/env python
"""
@package   document
Details:
Created:   Sunday, June 30th 2024, 8:36:38 pm
-----
Last Modified: 06/30/2024 11:00:59
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "document.py"
__version__ = "0.1.0"
from enum import Enum
from typing import List
from typing import Optional

from bs4 import BeautifulSoup

# from pydantic.schema import schema
from pydantic import Field

from .element import Element


class DocumentType(Enum):
    """An enumeration of the different types of documents."""

    GENERAL = "General"
    REQUIREMENTS = "Requirements"
    DESIGN = "Design"
    IMPLEMENTATION = "Implementation"
    TEST = "Test"
    DEPLOYMENT = "Deployment"
    OPERATION = "Operation"
    MAINTENANCE = "Maintenance"
    SUPPORT = "Support"
    TRAINING = "Training"
    USER_MANUAL = "User Manual"
    TECHNICAL_MANUAL = "Technical Manual"
    PRESENTATION = "Presentation"
    REPORT = "Report"
    PROPOSAL = "Proposal"
    SPECIFICATION = "Specification"
    PLAN = "Plan"


class DocumentSectionType(Enum):
    """An enumeration of the different types of document sections."""

    OVERVIEW = "Overview"
    INTRODUCTION = "Introduction"
    BACKGROUND = "Background"
    SCOPE = "Scope"
    OBJECTIVES = "Objectives"
    REQUIREMENTS = "Requirements"
    DESIGN_OVERVIEW = "Design Overview"
    ARCHITECTURE = "Architecture"
    COMPONENTS = "Components"
    INTERFACES = "Interfaces"
    DATA = "Data"
    ALGORITHMS = "Algorithms"
    TEST_PLAN = "Test Plan"
    TEST_CASES = "Test Cases"
    TEST_RESULTS = "Test Results"
    DEPLOYMENT_PLAN = "Deployment Plan"
    DEPLOYMENT_RESULTS = "Deployment Results"
    OPERATION_PLAN = "Operation Plan"
    OPERATION_RESULTS = "Operation Results"
    MAINTENANCE_PLAN = "Maintenance Plan"
    MAINTENANCE_RESULTS = "Maintenance Results"
    SUPPORT_PLAN = "Support Plan"


class DocumentSectionFormatType(Enum):
    SLIDE = "Slide"
    PAGE = "Page"
    CHAPTER = "Chapter"
    SECTION = "Section"
    SUBSECTION = "Subsection"
    PARAGRAPH = "Paragraph"
    BULLET = "Bullet"
    NUMBERED = "Numbered"
    TABLE = "Table"
    FIGURE = "Figure"
    EQUATION = "Equation"
    CODE = "Code"
    LIST = "List"
    REFERENCE = "Reference"
    FOOTNOTE = "Footnote"
    ENDNOTE = "Endnote"
    GLOSSARY = "Glossary"
    INDEX = "Index"
    APPENDIX = "Appendix"
    ANNEX = "Annex"
    ABBREVIATION = "Abbreviation"
    ACRONYM = "Acronym"
    SYMBOL = "Symbol"
    KEYWORD = "Keyword"
    SUMMARY = "Summary"


class DocumentSection(Element):
    type: Optional[DocumentSectionType] = Field(None, description="The type of the section.")
    sub_type: Optional[DocumentSectionFormatType] = Field(None, description="The format of the section.")
    section_level: Optional[int] = Field(None, description="The level of the section.")
    section_number: Optional[int] = Field(None, description="The number of the section.")
    document: Optional[str] = Field(None, description="The document the section belongs to.")
    page: Optional[int] = Field(None, description="The page the section belongs to.")
    parent_section_number: Optional[int] = Field(None, description="The parent section number.")
    author: Optional[str] = Field(None, description="The author of the section.")
    content: Optional[str] = Field(None, description="The content of the section.")
    section_length: Optional[int] = Field(None, description="The length of the section.")
    references: Optional[List[str]] = Field([], description="The references of the section.")
    summary: Optional[str] = Field(None, description="The summary of the section.")
    keywords: Optional[List[str]] = Field([], description="The keywords of the section.")
    related_sections: Optional[List[str]] = Field([], description="The related sections of the section.")


def html_to_docsections(html_content: str, document_name: str) -> List[DocumentSection]:
    soup = BeautifulSoup(html_content, "html.parser")
    sections = []
    section_number = 0

    for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        section_number += 1
        section_level = int(header.name[1])
        section_name = header.get_text()

        # Assuming section description might be in the next sibling paragraph
        section_description = None
        next_sibling = header.find_next_sibling()
        if next_sibling and next_sibling.name == "p":
            section_description = next_sibling.get_text()

        section_content = ""
        next_sibling = header.find_next_sibling()
        while next_sibling and next_sibling.name not in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            section_content += str(next_sibling)
            next_sibling = next_sibling.find_next_sibling()

        section = DocumentSection(
            name=section_name,
            section_level=section_level,
            section_description=section_description,
            document=document_name,
            section_number=section_number,
            content=section_content,
        )
        sections.append(section)

    return sections


class Document(Element):
    type: Optional[DocumentType] = Field(None, description="The type of the document.")
    section_ids: Optional[List[str]] = Field([], description="The section ids of the document.")
    summary: Optional[str] = Field(None, description="The summary of the document.")
    keywords: Optional[List[str]] = Field([], description="The keywords of the document.")
    references: Optional[List[str]] = Field([], description="The references of the document.")

    def load_from_html(self, html_content: str):
        self.sections = html_to_docsections(html_content, self.name)
        for section in self.sections:
            self.section_ids.append(section.id)

    def load_from_docx(self, docx_content: str):
        pass

    def load_from_pdf(self, pdf_content: str):
        pass

    # def load(self, filename: str):
    #     if filename.endswith(".html"):
    #         with open(filename) as file:
    #             html_content = file.read()
    #             self.load_from_html(html_content)
    #     elif filename.endswith(".docx"):
    #         with open(filename) as file:
    #             docx_content = file.read()
    #             self.load_from_docx(docx_content)


class FileType(Enum):
    """An enumeration of the different types of files."""

    TEXT = "Text"
    IMAGE = "Image"
    AUDIO = "Audio"
    VIDEO = "Video"
    DOCUMENT = "Document"
    SPREADSHEET = "Spreadsheet"
    PRESENTATION = "Presentation"
    DATABASE = "Database"
    CODE = "Code"
    EXECUTABLE = "Executable"
    ARCHIVE = "Archive"
    COMPRESSED = "Compressed"
    DISK_IMAGE = "Disk Image"
    VIRTUAL_MACHINE = "Virtual Machine"
    CONFIGURATION = "Configuration"
    LOG = "Log"
    BACKUP = "Backup"
    TEMPORARY = "Temporary"
    SYSTEM = "System"
    WEB = "Web"
    EMAIL = "Email"
    CONTACT = "Contact"
    CALENDAR = "Calendar"
    NOTE = "Note"
    BOOKMARK = "Bookmark"
    LINK = "Link"
    REFERENCE = "Reference"
    TEMPLATE = "Template"
    FORM = "Form"
    SURVEY = "Survey"
    QUESTIONNAIRE = "Questionnaire"
    POLL = "Poll"
    QUIZ = "Quiz"
    EXAM = "Exam"
    TEST = "Test"
    SURVEILLANCE = "Surveillance"
    MONITORING = "Monitoring"
    AUDIT = "Audit"
    INSPECTION = "Inspection"
    REVIEW = "Review"
    EVALUATION = "Evaluation"
    ASSESSMENT = "Assessment"
    ANALYSIS = "Analysis"
    REPORT = "Report"
    PROPOSAL = "Proposal"
    SPECIFICATION = "Specification"
    PLAN = "Plan"
    AGREEMENT = "Agreement"
    CONTRACT = "Contract"
    LICENSE = "License"
    CERTIFICATE = "Certificate"
    DIPLOMA = "Diploma"
    DEGREE = "Degree"


class FileDocument(Document):
    type: Optional[FileType] = Field(None, description="The type of the file.")
    file_path: Optional[str] = Field(None, description="The path of the file.")
    file_size: Optional[int] = Field(None, description="The size of the file.")
    file_format: Optional[str] = Field(None, description="The format of the file.")
    file_ext: Optional[str] = Field(None, description="The extension of the file.")
