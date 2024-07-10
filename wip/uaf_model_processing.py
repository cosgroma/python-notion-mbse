from lxml import etree
from pydantic import BaseModel, create_model
from xml.etree import ElementTree as ET
import json
import sys
import xml
import xmltodict
from typing import Any

def parse_xmi(file_path: str) -> ET.Element:
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def extract_classes(xmi_root: ET.Element) -> list:
    classes = []
    for elem in xmi_root.findall(".//UML:Class", namespaces={"UML": "http://www.omg.org/spec/UML/20090901"}):
        class_name = elem.get("name")
        attributes = []
        for attr in elem.findall(".//UML:Attribute", namespaces={"UML": "http://www.omg.org/spec/UML/20090901"}):
            attr_name = attr.get("name")
            attr_type = attr.get("type")
            attributes.append((attr_name, attr_type))
        classes.append((class_name, attributes))
    return classes

def extract_stereotypes(profile_root):
    stereotypes = {}
    for elem in profile_root.findall(".//UML:Stereotype", namespaces={"UML": "http://www.omg.org/spec/UML/20090901"}):
        stereotype_name = elem.get("name")
        stereotypes[stereotype_name] = stereotype_name  # This could be expanded to more complex structures
    return stereotypes

def parse_xml_to_dict(xml_file_path: str):
    """
    Parse the XML file and convert it to a Python dictionary.

    :param xml_file_path: Path to the XML file.
    :return: Dictionary representation of the XML.
    """
    with open(xml_file_path, 'r') as file:
        xml_string = file.read()
    return xmltodict.parse(xml_string)

def process_xmi_to_pydantic(file_path):
    xmi_root = parse_xmi(file_path)
    classes = extract_classes(xmi_root)
    models = [create_pydantic_model(class_name, attributes) for class_name, attributes in classes]
    return models

def create_stereotype_base_classes(stereotypes):
    base_classes = {}
    for name in stereotypes:
        base_classes[name] = type(name, (BaseModel,), {})
    return base_classes

def parse_xml(xml_file_path: str):
    # Parsing the XMI file
    try:
        # Parse the XMI content
        # Reading the content of the file
        with open(xml_file_path, 'r') as file:
            xmi_content = file.read()
            # print(xmi_content)
        # tree = etree.parse(xml_file_path)
        tree = ET.ElementTree(ET.fromstring(xmi_content))
        root = tree.getroot()

        # Basic parsing: Extracting elements and their attributes
        elements = []
        for element in root.iter():
            # Extract element tag and attributes
            element_data = {
                'tag': element.tag,
                'attributes': element.attrib
            }
            # print(element_data)
            elements.append(element_data)

        # Show the first few elements to understand the structure
        
    except Exception as e:
        sample_elements, error_message = None, str(e)


    return elements



# Function to create a basic JSON Schema from the parsed XMI elements
def create_json_schema(elements):
    # Initial structure of the JSON Schema
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {}
    }

    # Iterate through the elements to populate the JSON Schema
    for element in elements:
        # Use element tag as key
        key = element['tag'].split('}')[-1]  # Removing namespace

        
        # Add a basic structure for each element
        json_schema["properties"][key] = {
            "type": "object",
            "properties": {}
        }

        # Add attributes of the element
        for attr, value in element['attributes'].items():
            print(attr)
            attr_key = attr.split('}')[-1]  # Removing namespace
            json_schema["properties"][key]["properties"][attr_key] = {
                "type": "string",  # Assuming string type for simplicity
                "example": value
            }

    return json_schema


def generate_pydantic_model(data_dict: dict):
    """
    Generate a Pydantic model based on the dictionary.

    :param data_dict: Dictionary containing the XML data.
    :return: Pydantic model class.
    """
    # Dynamically create a Pydantic model
    return create_model('DynamicModel', **{k: (type(v), ...) for k, v in data_dict.items()})

def create_pydantic_model(class_name, attributes):
    model_fields = {attr[0]: (Any, None) for attr in attributes}  # Default to Any type for simplicity
    return type(class_name, (BaseModel,), model_fields)

def main():
    """
    Main function to convert XML to JSON schema.
    """
    # xml_file_path = '/home/cosgroma/workspace/tools/ngira/apps/progman/UAF.xmi.xml'
    xml_file_path = sys.argv[1]
    sample_elements = parse_xml(xml_file_path)
    # pydantic_model = generate_pydantic_model(data_dict)
    # Creating a JSON Schema from the extracted elements
    basic_json_schema = create_json_schema(sample_elements)

    # Displaying the basic JSON Schema
    print(json.dumps(basic_json_schema, indent=4))
    # Generate JSON schema
    # json_schema = pydantic_model.schema()
    # print(json.dumps(json_schema, indent=2))

if __name__ == "__main__":
    main()
