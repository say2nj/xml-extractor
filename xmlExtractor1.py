import xml.etree.ElementTree as ET
tree = ET.parse("G://Python/sample.xml")
root = tree.getroot()
levels= root.findall('./book')
f= open("newXML.xml","w+")
f.write('<?xml version="1.0"?>\n<catalog>\n')
for level in levels:
    id= level.get('id')
    title = level.find('title').text
    price = float(level.find('price').text)
    desc = level.find('description').text
    f.write('\t<book id="'+id)
    f.write('">\n')
    f.write('\t\t<title>')
    f.write(title)
    f.write('</title>\n\t\t<desc>')
    f.write(desc)
    f.write('</desc>\n\t\t<price>')
    f.write(str(price))
    f.write('</price>\n\t</book>\n\n')
f.write('</catalog>')
f.close()
print ("Your XML file has been extracted and is saved as newXML.xml file in python directory")
