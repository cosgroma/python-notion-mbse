import xmlschema


class SchemaParser:
    def __init__(self, schema_file: str):
        self.schema_file = schema_file
        self.xs = xmlschema.XMLSchema(schema_file)

    def get_dict(self, xml_file: str):
        return self.xs.to_dict(xml_file)


XMI_SCHEMA = "model/XMI.xsd"
XmiParser = SchemaParser(XMI_SCHEMA)

ECORE_SCHEMA = "model/Ecore.xsd"
EcoreParser = SchemaParser(ECORE_SCHEMA)
ECOREXMI_SCHEMA = "model/EcoreXMI.xsd"
EcoreXmiParser = SchemaParser(ECOREXMI_SCHEMA)
