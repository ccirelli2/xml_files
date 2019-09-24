# Import Modules
import xml.etree.ElementTree as ET
import os

# Import File
dir_xml_files = '/home/ccirelli2/Desktop/GSU/gsu_image_processing/Project_1/data/xml'
os.chdir(dir_xml_files)
list_files = os.listdir(dir_xml_files)


# Iterate Tree, Build Dictionary
def parse_xml_return_dict(xml_file):
    # Read File
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Create Dict Object
    plate_dict_values = {}

    # Iterate Tree and Extract X, Y, Widgth, Height Key/Value Pairs 
    for child in root:
        if child.tag == 'PlateXCoord':
            plate_dict_values['PlateXCoord'] = int(child.text)
        elif child.tag == 'PlateYCoord':
            plate_dict_values['PlateYCoord'] = int(child.text)
        elif child.tag == 'PlateWidth':
            plate_dict_values['PlateWidth'] = (child.text)
        elif child.tag == 'PlateHeight':
            plate_dict_values['PlateHeight'] = (child.text)
    
    # Return Dictionary
    return plate_dict_values


for num in range(0,10):
    plate_info = parse_xml_return_dict(list_files[num])
    print(plate_info)

