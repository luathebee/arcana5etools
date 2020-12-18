import json


items = []
baseItem = {
    "name": "",
    "type": "",
    "rarity": "",
    "source": "AotA",
    "entries": []
}
totalItems = 0
currentItem = {}
setType = False
descriptionLine = []
descriptionList = []

file = open("AotAItems.txt","r")

for line in file :
    #-------------------------------------------------------------
    if line.isupper():
        totalItems += 1
        print("\nCurrent item for reference")
        print(currentItem)
        #closes last entry
        items.append(currentItem.copy())

        #starts new item
        currentItem = baseItem.copy()
        descriptionList = []
        #currentItem["entries"][:] = [].copy()

        #sets the name
        currentItem["name"] = line.lower().strip("\n")

        #enable setType mode
        setType = True
        continue
    #-------------------------------------------------------------
    elif setType == True:
        if not line.isspace():
            if "Cypher" in line:
                currentItem["type"] = "CY"
            elif "Relic" in line:
                currentItem["type"] = "RLC"
            elif "Iron" in line:
                currentItem["type"] = "IF"
            if "uncommon" in line:
                currentItem["rarity"] = "uncommon"
            elif "common" in line:
                currentItem["rarity"] = "common"
            elif "very rare" in line:
                currentItem["rarity"] = "very rare"
            elif "rare" in line:
                currentItem["rarity"] = "rare"
            elif "legendary" in line:
                currentItem["rarity"] = "legendary"
            if "attunement" in line:
                currentItem["reqAttune"] = True
            setType = False
        continue
    #-------------------------------------------------------------
    # sets description
    #setDescription(currentItem, line)
    if line.isspace():
        if descriptionLine != []:
            descriptionList.append(" ".join(descriptionLine.copy())) #if white space, writes list as a description line
            currentItem["entries"] = descriptionList.copy() #copies current descList to avoid overwrite
            descriptionLine[:] = []
        continue
    else:
        descriptionLine.append(line.strip("\n")) #writes line to descritpion line list

#when its over, passes over last item
descriptionList.append(" ".join(descriptionLine.copy()))
currentItem["entries"] = descriptionList.copy()
print("\nCurrent item for reference")
print(currentItem)
#closes last entry
totalItems += 1
items.append(currentItem.copy())

print("++-+-++-+-++-++-++-+-++-++-++-++-++-+++-+++-+++-+")
print("\n Total items for reference :" ,totalItems)

# writes items to json output, must exist first 
out_file = open("test1.json", "w")
json.dump(items, out_file, indent=4)
out_file.close()
