# import os

# from pyecore.resources import URI
# from pyecore.resources import ResourceSet
# from xsd_utils import EcoreXmiParser


# def load_model_root(filename):
#     rset = ResourceSet()
#     resource = rset.get_resource(URI(filename))
#     mm_root = resource.contents[0]
#     rset.metamodel_registry[mm_root.nsURI] = mm_root
#     print(f"Loaded {filename}")
#     print(f"Model root: {mm_root}")
#     return rset
#     # At this point, the .ecore is loaded in the 'rset' as a metamodel
#     # resource = rset.get_resource(URI('path/to/instance.xmi'))
#     # model_root = resource.contents[0]
#     # # At this point, the model instance is loaded!
#     # return model_root


# import json


# def main():
#     home_dir = os.path.expanduser("~")
#     sgt_kb = os.path.join(home_dir, "workspace", "sergeant", ".sgt-kb")
#     model_files = os.listdir(sgt_kb)
#     model_files = [os.path.join(sgt_kb, f) for f in model_files if f.endswith(".ecore")]
#     for file in model_files:
#         # try:
#         print(f"Processing {file}")
#         output_dict = EcoreXmiParser.get_dict(file)
#         rset = load_model_root(file)
#         output_filename = file.replace(".ecore", ".json")
#         with open(output_filename, "w") as f:
#             json.dump(output_dict, f, indent=4)
#         # except Exception as e:
#         #     print(f"Failed to parse {file} - {e.with_traceback(None)}")
#         #     raise e


# if __name__ == "__main__":
#     main()
