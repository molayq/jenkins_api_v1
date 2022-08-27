import yaml


# yaml = ruamel.yaml.YAML()
# data = yaml.load(in_file)
with open("users.yml") as f:
     list_doc = yaml.safe_load(f)

print(list_doc["jenkins"]["authorizationStrategy"]["projectMatrix"]["permissions"])

y = list_doc["jenkins"]["authorizationStrategy"]["projectMatrix"]["permissions"]

list_doc["jenkins"]["authorizationStrategy"]["projectMatrix"]["permissions"].append('USER:Agent/Build:coco')


with open("data.yml", "w", encoding = "utf-8") as yaml_file:
    dump = yaml.dump(list_doc, default_flow_style = False, allow_unicode = True, encoding = None, default_style='"')
    yaml_file.write( dump)