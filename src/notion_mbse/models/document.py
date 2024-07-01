#!/usr/bin/env python
"""
@package   document
Details:
Created:   Sunday, June 30th 2024, 8:36:38 pm
-----
Last Modified: 06/30/2024 09:02:30
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "document.py"
__version__ = "0.1.0"
from enum import Enum
from typing import List
from typing import Optional

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


class Document(Element):
    name: Optional[str] = Field(None, description="The name of the document.")
    type: Optional[DocumentType] = Field(None, description="The type of the document.")
    section_ids: Optional[List[str]] = Field([], description="The section ids of the document.")
    # @model_serializer
    # def ser_model(self) -> Dict[str, Any]:
    #     return {
    #         "id": str(self.id),
    #         "name": self.name,
    #         "description": self.description,
    #         "version": self.version,
    #         "tags": self.tags,
    #         "type": self.type,
    #         "sub_type": self.sub_type,
    #         "created_by": self.created_by,
    #         "created_at": self.created_at,
    #         "modified_by": self.modified_by,
    #         "modified_at": self.modified_at,
    #         "status": self.status,
    #         "documentation": self.documentation,
    #         "ref_ids": self.ref_ids
    #     }


# # Example usage
# section = DocumentSection(
#     name="Introduction",
#     section_level=1,
#     section_description="This is the introduction section.",
#     document="Example Document",
#     section_number=1,
#     content="The content of the introduction section.",
#     section_length=100,
#     references=["Ref1", "Ref2"],
#     tags=["intro", "overview"],
#     creation_date=datetime.now(),
#     modification_date=datetime.now(),
#     author="John Doe",
#     summary="A brief overview of the introduction.",
#     related_sections=["Section 2", "Section 3"],
#     section_id="12345",
# )

# print(section.json(indent=2))
