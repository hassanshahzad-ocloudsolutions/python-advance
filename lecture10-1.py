#XML(Extensible Markup Language)Processing in python
'''XML (eXtensible Markup Language) is used to store, structure, and transfer data between systems in a 
platform-independent, application independent and human-readable format.
It is like a universal container for data, especially when different programs, languages, or platforms need 
to understand each other.
Use to heirarchical structure the data.

Two ways to work with XML SAX or DOM(Never loads full XML in RAM. It is useful when we have very large XML files)

When two systems (maybe built in different languages — Python, Java, PHP) need to 
exchange data, XML provides a standard format everyone can understand ie Application Independent

XML is just plain text, so it works on any operating system, database, or language ie Platform Independent

Simple XML examples

<employee id=1107>
    <name>Hassan Shahzad</name>
    <age>21</age>
    <department>IT</department>
</employee>

<school id = 1>
  <student id=007>
    <name>Ali</name>
    <subjects>
      <subject>Math</subject>
      <subject>English</subject>
    </subjects>
  </student>
</school>

SAX (Simple API for XML) parser works event-driven —
it reads XML sequentially (line by line) and triggers events (like “start tag”, “end tag”, “text found”).
It does not load the entire XML into memory. Read-Only


DOM(Document Object Model) parser reads the entire XML document into memory, and 
represents it as a tree structure of nodes (elements, attributes, text, etc.).
That means — the whole XML file is loaded at once, and you can traverse, modify, or search any part of it.
'''

import xml.sax as xsax#read only and memory efficient(as it loads only specific portion from xml file)
#handler(works with the file) and parser(translates xml into python scripts) is needed

class GroupHandler(xsax.ContentHandler):
    #first function to be called when we get into an element
    ''''Called whenever an opening tag (<tag>) is found. 
    name: the tag name
    attrs: the attributes of that tag (like id="1")'''

    '''name contains the ame of the tag. attrs contains the key value pair of specific tag'''
    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'employee':
            print("----Employee---")
            print(f"ID of the employee is {attrs['id']}")
    
 
    '''Handles tag content in accordance to condition set in the startElement function'''
    def characters(self, content):
        content = content.strip()

        if not content:
            return  # ignore whitespace
        if self.current == 'first_name': #from startElement
            self.name = content
        elif self.current == 'last_name':
            self.lname = content
        elif self.current == 'age':
            self.age = content
        elif self.current == 'position':
            self.position = content
        elif self.current == 'salary':
            self.salary = content
        elif self.current == 'location':
            self.location = content
    
    '''Called whenever a closing tag (</tag>) is found.'''
    def endElement(self,name):
        if self.current == 'first_name': #from startElement
            print(f'First Name: {self.name}')
        elif self.current == 'last_name':
            print(f'Last Name: {self.lname}')
        elif self.current == 'age':
            print(f'Age: {self.age}')
        elif self.current == 'position':
            print(f'Position: {self.position}')
        elif self.current == 'salary':
            print(f'Salary: {self.salary}')
        elif self.current == 'location':
            print(f'Location: {self.location}')
        self.current = ''
        

        
    
handler = GroupHandler()
parser = xsax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')




 