#open file
with open("templete_squished.txt", 'r') as template:
    data = template.read()

########~~~~PASS 1 - Python Datastructures~~~~########

#split into feilds
feilds = data.split(";")

#remove trailng blank entries (usually only one)
while feilds[-1].strip() == '':
    _temp = feilds.pop(-1)

#split each feild into label [0] and contents [1]
split_feilds = [];
for feild in feilds:
    split_feilds.append(feild.split(":"))

#try and set module name
for feild in split_feilds:
    name_found = False
    if feild[0] == "Name":
        Name = feild[1]
        name_found = True
        break
#raise an error if the name could not be found
if not name_found:
    raise NameError("FORMAT ERROR: A name is required for all modules!")

#try and set library name
for feild in split_feilds:
    lib_found = False
    if feild[0] == "Library":
        Library = feild[1]
        lib_found = True
        break
#raise an error if the library could not be found
if not lib_found:
    raise NameError("FORMAT ERROR: All modules must be in a library!")

#try and find the inputs
for feild in split_feilds:
    inputs_found = False
    if feild[0] == "Inputs":
        Inputs = feild[1].split(",")
        inputs_found = True
        break
#raise an error if the inputs could not be found
if not inputs_found:
    raise NameError("FORMAT ERROR: Inputs are required for all modules!")

#try and find the outputs
for feild in split_feilds:
    outputs_found = False
    if feild[0] == "Outputs":
        Outputs = feild[1].split(",")
        outputs_found = True
        break
#raise an error if the outputs could not be found
if not outputs_found:
    raise NameError("FORMAT ERROR: Outputs are required for all modules!")

#try and find the libraries to import, if any
Import = []
for feild in split_feilds:
    if feild[0] == "Import":
        Import = feild[1].split(",")
        break

#try and find parts, if any
Parts = []
for feild in split_feilds:
    if feild[0] == "Parts":
        parts_temp = feild[1].split(",")
        for part in parts_temp:
            Parts.append(part.split("#"))
        break

#try and find the wires (more splitting will be done later)
for feild in split_feilds:
    wires_found = False
    if feild[0] == "Wires":
        Wires = feild[1].split(",")
        wires_found = True
        break
#raise an error if the wires could not be found
if not wires_found:
    raise NameError("FORMAT ERROR: Wires are required for all modules!")

