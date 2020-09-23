import xml.etree.ElementTree as ET
tree = ET.parse("G://Python/sample.xml")
root = tree.getroot()
levels= root.findall('./book')
for level in levels:
    title = level.find('title').text
    price = float(level.find('price').text)
    desc = level.find('description').text
    print ("<title>",title,"</title>\n<desc>",desc,"</desc>\n<price>",price,"</price>\n\n")
