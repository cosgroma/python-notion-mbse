from openai import OpenAI
import os
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

import os
from pathlib import Path
from shutil import copyfile



def extract_filenames(mkdocs_content):
    filenames = []
    for line in mkdocs_content.split("\n"):
        if ".md" in line:
            filenames.append(line.split(":")[1].strip())
    return filenames

def copy_files(filenames, output_dir):
    for filename in filenames:
        print(f"Copying {filename} to {output_dir}")
        copyfile(filename, os.path.join(output_dir, Path(filename).name))

def create_files(filenames, output_dir) -> List[str]:
    created_files = []
    for filename in filenames:
        print(f"Creating {filename} in {output_dir}")
        full_filename = os.path.join(output_dir, filename)
        dirname = os.path.dirname(full_filename)
        Path(dirname).mkdir(parents=True, exist_ok=True)
        Path(full_filename).touch()
        created_files.append(full_filename)
    return created_files

def get_filenames(filenames, output_dir) -> List[str]:
    created_files = []
    for filename in filenames:
        full_filename = os.path.join(output_dir, filename)
        created_files.append(full_filename)
    return created_files
        

def extract_nav(mkdocs_content):
    return mkdocs_content.split("nav:")[1].split("plugins:")[0].strip()

doc_dict = {
    "sergeant_design_docs": {
      "content": 
'''
site_name: SERGEANT Design System Documentation
site_description: Comprehensive guide to the SERGEANT Design System for embedded systems.

theme:
  name: material

nav:
  - Home: index.md
  - SERGEANT Design Overview:
      - Introduction: sergeant_design/introduction.md
      - Properties: sergeant_design/properties.md
      - Relationships: sergeant_design/relationships.md
  - FPGA Subsystem Design:
      - Overview: fpga_subsystem/overview.md
      - Design Collections: fpga_subsystem/design_collections.md
      - Configuration Files: fpga_subsystem/configuration_files.md
      - Relationships: fpga_subsystem/relationships.md
  - Software Subsystem Design:
      - Overview: software_subsystem/overview.md
      - Processing Channels: software_subsystem/processing_channels.md
      - Startup Scripts: software_subsystem/startup_scripts.md
      - Application and Service Configuration: software_subsystem/application_service_configuration.md
      - Relationships: software_subsystem/relationships.md
  - Additional Resources:
      - FAQs: additional_resources/faqs.md
      - Glossary: additional_resources/glossary.md
      - Contact: additional_resources/contact.md

plugins:
  - search
  - mkdocs-git-revision-date-localized-plugin

markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
'''
    },
}


for doc_package in doc_dict:
    print(f"Creating {doc_package}")
    output_dir = doc_package
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    mkdocs_content = doc_dict[doc_package]['content']
    # create_files(filenames, output_dir)
    doc_dict[doc_package]["files"] = get_filenames(extract_filenames(mkdocs_content), output_dir)
    doc_dict[doc_package]["nav"] = extract_nav(mkdocs_content)

def get_message_set(prompt: str) -> List[Dict[str, Any]]:
        return [
    {
      "role": "system",
      "content": ""
    },
    {
      "role": "user",
      "content": "I am working on design documentation. We are working on this file: index.md\n\nHere is where it fits in the larger documentation structure:\n- Home: index.md\n  - SERGEANT Design Overview:\n      - Introduction: sergeant_design/introduction.md\n      - Properties: sergeant_design/properties.md\n      - Relationships: sergeant_design/relationships.md\n  - FPGA Subsystem Design:\n      - Overview: fpga_subsystem/overview.md\n      - Design Collections: fpga_subsystem/design_collections.md\n      - Configuration Files: fpga_subsystem/configuration_files.md\n      - Relationships: fpga_subsystem/relationships.md\n  - Software Subsystem Design:\n      - Overview: software_subsystem/overview.md\n      - Processing Channels: software_subsystem/processing_channels.md\n      - Startup Scripts: software_subsystem/startup_scripts.md\n      - Application and Service Configuration: software_subsystem/application_service_configuration.md\n      - Relationships: software_subsystem/relationships.md\n  - Additional Resources:\n      - FAQs: additional_resources/faqs.md\n      - Glossary: additional_resources/glossary.md\n      - Contact: additional_resources/contact.md\n\nHere is some relevant background that will help you create a good markdown outline for the index.md file:\n\n\n## SERGEANT Design\n\n- **Description:** The SERGEANT Design is a framework for setting up embedded systems. It brings together software and hardware parts smoothly. This is vital in complex embedded system designs where these two need to work together.\n- **Properties:**\n    - **Design Name:** This is the specific name of the design. It helps tell designs apart and make sure the right one is used or updated.\n    - **Environment Variables and Paths:** These properties set up and manage the system's behavior. Environment variables are dynamic-named values that can change how running processes behave. They're part of the process's environment.\n- **Relationships:** The SERGEANT Design Documentation shows how components connect and interact. It includes FPGA and Software Subsystem Designs. The FPGA Subsystem Designs set up the digital logic of the embedded system. The Software Subsystem Designs set up the software structure. Both are important parts of the design documentation, making sure that the hardware and software are designed to work together. The framework also brings in various Design Components, giving a full view of the system's design and making it easier to understand and update.\n\n**2. FPGA Subsystem Design**\n\n- **Description:** This role mainly manages hardware parts within a system. It focuses on the development of Field Programmable Gate Array (FPGA) components. The role needs a deep understanding of how hardware parts work and interact, and how they connect with software parts.\n- **Properties:**\n    - **Design Collections:** These are different sets of design configurations that this role manages. Examples include baseline and player. These collections organize the different configurations needed for the system.\n    - **Configuration Files:** This role also manages different types of configuration files. These include Tool Command Language (TCL) files, Xilinx Design Constraints (XDC) files, and system topology files. Each file type has a unique role in setting up the hardware parts and the system as a whole.\n- **Relationships:** This role interacts a lot with the Software Subsystem Design. It supports this subsystem by providing the necessary hardware infrastructure. This means the hardware management role needs to understand the software subsystem's needs and capabilities, and be able to work well with the team managing the software subsystem.\n\n**3. Software Subsystem Design**\n\n- **Description:** The software elements category is comprised of various components such as applications, daemons, and engines. These elements play a crucial role in the functionality and operation of the software.\n- **Properties:**\n    - Configurable Processing Channels: These channels allow for the customization and adjustment of processing capabilities to suit specific needs and requirements.\n    - Startup Scripts: These are sets of instructions that are executed automatically when the system boots up. They are instrumental in setting up the initial configuration and defining the behavior of the software.\n    - Application and Service Configuration: This refers to the settings and parameters that dictate the behavior and functioning of both applications and services within the system.\n- **Relationships:** The software elements utilize FPGA Subsystem Designs, which are integral to the operation of the software. Furthermore, they interact with various components within the system to ensure seamless functionality. These interactions contribute significantly to the overall runtime environment, playing a pivotal role in software execution and performance.\n\n"
    },
    {
      "role": "assistant",
      "content": "# Home\n\nWelcome to the main page of the SERGEANT Design Documentation. This document serves as a central hub directing you to various sections that elaborate on the design, implementation, and configuration of our sophisticated embedded system frameworks, including both hardware and software components.\n\nBelow are listed the primary sections of the SERGEANT Design Documentation. This guide is structured to provide a comprehensive understanding of the system.\n\n## [SERGEANT Design Overview](sergeant_design/introduction.md)\nThe SERGEANT Design framework is dedicated to integrating software and hardware components of embedded systems. Explore this section for a thorough introduction and detailed insights into the properties and relationships within the system.\n\n- [Introduction](sergeant_design/introduction.md)\n- [Properties](sergeant_design/properties.md)\n- [Relationships](sergeant_design/relationships.md)\n\n## [FPGA Subsystem Design](fpga_subsystem/overview.md)\nThe FPGA Subsystem Design focuses on configuring and managing the hardware elements of the system. Take a look at an overview and delve into the design collections, configuration files, and the interplay between FPGA and software components.\n\n- [Overview](fpga_subsystem/overview.md)\n- [Design Collections](fpga_subsystem/design_collections.md)\n- [Configuration Files](fpga_subsystem/configuration_files.md)\n- [Relationships](fpga_subsystem/relationships.md)\n\n## [Software Subsystem Design](software_subsystem/overview.md)\nGain insight into the design of the software elements which are integral to system functionality. Here you'll find information on processing channels, startup scripts, application and service configurations, as well as the relationships they have with other system components.\n\n- [Overview](software_subsystem/overview.md)\n- [Processing Channels](software_subsystem/processing_channels.md)\n- [Startup Scripts](software_subsystem/startup_scripts.md)\n- [Application and Service Configuration](software_subsystem/application_service_configuration.md)\n- [Relationships](software_subsystem/relationships.md)\n\n## Additional Resources\nIf you have further questions or require more detailed definitions, our additional resources provide assistance with FAQs, a glossary of terms, and contact information for direct support.\n\n- [FAQs](additional_resources/faqs.md)\n- [Glossary](additional_resources/glossary.md)\n- [Contact](additional_resources/contact.md)\n\nWe encourage you to explore each section in depth to fully understand the intricacies of the SERGEANT Design framework and how its various subsystems are designed to interoperate seamlessly.\n"
    },
    {
        "role": "user",
        "content": prompt
    }
  ]

def estimate_tokens(message_set: List[Dict[str, Any]]) -> int:
    tokens = 0
    for message in message_set:
        tokens += len(message['content'].split(" "))
    return tokens

def get_mardown_content(prompt: str) -> str:
  token_size = estimate_tokens(get_message_set(prompt))
  response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=get_message_set(prompt),
      temperature=1.7,
      max_tokens=2*token_size,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
  )

  return response

# Documenation Generation Template
CREATE_DOCUMENT_FROM_CONTEXT_TEMPLATE = """
I am working on design documentation. We are working on this file: {filename}

Here is where it fits in the larger documentation structure:

---

{nav}

---

Here is some relevant background that will help you create a good markdown outline for the {filename} file:

---

{context}

---

Remember to:

- Ensure clarity and technical accuracy, suitable for a professional audience.
- Include links to related subsections under each main section as provided in the structure.
- Use the appropriate formatting for each section and subsection.
- Use the appropriate headings for each section and subsection.

We have done great work so far. I have been very pleased with the progress we have made. I am excited to see what we can do next.

"""


# doc_package = "sergeant_design_docs"
# for filename in doc_dict[doc_package]["files"]:
#     if os.path.basename(filename) == "index.md":
#         continue
#     print(f"Creating outline for {os.path.basename(filename)}")

#     outline = CREATE_DOCUMENT_FROM_CONTEXT_TEMPLATE.format(
#       filename=os.path.basename(filename), 
#       context=PROJECT_DOCUMENTATION, 
#       nav=doc_dict[doc_package]["nav"]
#     )
#     doc_dict[doc_package][filename] = get_mardown_content(outline)
#     break