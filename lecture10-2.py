#DOM(Document Object Model)
#When working with DOM we can update the values as well of tags

import xml.dom.minidom as dom

domtree = dom.parse('data.xml')
group = domtree.documentElement #root of dom tree
print(group.getAttribute('name')) #print whatever name of root element is
employees = group.getElementsByTagName('employee')

for employee in employees:
    print("---Employee----")
    if employee.hasAttribute('id'):
        print(f'ID: {employee.getAttribute('id')}')
        print(f'first_name: {employee.getElementsByTagName('first_name')[0].childNodes[0].data}')
        print(f'last_name: {employee.getElementsByTagName('last_name')[0].childNodes[0].data}')
        print(f'age: {employee.getElementsByTagName('age')[0].childNodes[0].data}')
        print(f'position: {employee.getElementsByTagName('position')[0].childNodes[0].data}')
        print(f'salary: {employee.getElementsByTagName('salary')[0].childNodes[0].data}')
        print(f'location: {employee.getElementsByTagName('location')[0].childNodes[0].data}')


#updating the xml file via dom manipulation

employees[2].getElementsByTagName('first_name')[0].childNodes[0].nodeValue = "Shahzad"
employees[1].setAttribute('id','69')
domtree.writexml(open('data.xml','w'))

#creating new employee

departments = group.getElementsByTagName('department')
engineering = departments[0]
new_employee = domtree.createElement('employee')
new_employee.setAttribute('id', '303')

first_name = domtree.createElement('first_name')
first_name.appendChild(domtree.createTextNode('Bilal'))
new_employee.appendChild(first_name)

last_name = domtree.createElement('last_name')
last_name.appendChild(domtree.createTextNode('Ahmed'))
new_employee.appendChild(last_name)

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('26'))
new_employee.appendChild(age)

position = domtree.createElement('position')
position.appendChild(domtree.createTextNode('DevOps Engineer'))
new_employee.appendChild(position)

salary = domtree.createElement('salary')
salary.appendChild(domtree.createTextNode('105000'))
new_employee.appendChild(salary)

location = domtree.createElement('location')
location.appendChild(domtree.createTextNode('Islamabad'))
new_employee.appendChild(location)

engineering.appendChild(new_employee)

domtree.writexml(open('data.xml','w'))


