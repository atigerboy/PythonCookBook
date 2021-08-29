class XMLNamespaces:
    def __init__(self,**kwargs):
        self.namespaces={}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = f'{{{uri}}}'
    def __call__(self, path):#instance as function
        return path.format_map( self.namespaces )#string format_map( dictionary )


xml_str='''
<top>
    <author>David Beazley</author>
    <content>
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>Hello World</title>
            </head>
            <body>
                <h1>Hello World!</h1>
            </body>
        </html>
    </content>
</top>
'''
ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
from xml.etree.ElementTree import parse,fromstring, Element

doc = fromstring(xml_str) #parse('ns.xml')
print( ns('content/{html}html') )
print( doc.find(ns('content/{html}html')))
print( doc.findtext(ns('content/{html}html/{html}head/{html}title')) )