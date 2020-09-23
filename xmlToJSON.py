#install xmltodict package, pip install xmltodict 
import json
import xmltodict

with open("G://Python/sample.xml") as xml_file:
    xml_content = xmltodict.parse(xml_file.read())
    xml_file.close()

    json_content=json.dumps(xml_content)

    with open("G://Python/sample.json","w") as json_file:
        json_file.write(json_content)
        json_file.close()

print("XML file has been parsed into JSON file");
