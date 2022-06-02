#nguay089 is my username.
# import csv and sys module package
import csv
import sys
#method to convert from csv to xml format. 
def convert_file():
    # READ the csv file
    csv_data=sys.argv[1] 
    csv_file = csv.reader(open(csv_data))
    #load_csv_data = csv.reader(csv_file)
    # READ the xml file
    xml_file = 'FileXML.xml'
    load_xml_data = open(xml_file, 'w')
    #initialize the Self-Describing tag.
    load_xml_data.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
    # the start tags will be added
    load_xml_data.write('<newline>' + "\n")
    index = 0
    # with each row in the csv file, for loop will load the content into the tags. 
    for row in csv_file: 
        if index == 0:
            #Load the empty content in the elements
            elements = row
            for i in range(len(elements)):
                elements[i] = elements[i].replace(' ', '_')
        else:
            load_xml_data.write("\t" +'<column>' + "\n")
            for i in range(len(elements)):
                load_xml_data.write('\t\t' + '<' + elements[i] + '>' + row[i] + '</' + elements[i] + '>' + "\n")
            load_xml_data.write("\t" + '</column>' + "\n")
        index += 1
# Add the end tags.
    load_xml_data.write('</newline>' + "\n")
    load_xml_data.close()

if __name__ == '__main__':
    convert_file()
