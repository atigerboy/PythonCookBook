from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()

root.remove(root.find('sri'))
root.remove(root.find('cr'))

#getchildren
for index, val  in enumerate( root ):
    if val.tag == 'nm':
        e = Element('spam')
        e.text = 'This is a tree'
        root.insert( index+1, e)
        break

doc.write('newpred.xml', xml_declaration=True)