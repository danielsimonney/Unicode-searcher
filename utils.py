import unicodedata
def UnicodeEnter(EntryPoint):
    a_bool = 'U+' in EntryPoint
    if(EntryPoint.isdigit()==True):
        return TraductNumber(EntryPoint)
    if(a_bool==True):
        return TraductHexa(EntryPoint)
    elif(len(EntryPoint)==1):
        return TraductUnicode(EntryPoint)
    else:
        return TraductLetter(EntryPoint)

def result(uniNumber,uniName,searchNumber):
    Informations=dict()
    Informations[0] = {} 
    Informations[0]['name']=uniName
    Informations[0]['number']=int(searchNumber)
    Informations[0]['unicode']=u""+uniNumber+""
    return Informations

def TraductNumber(EntryPoint):
    Num =EntryPoint
    character = chr(int(EntryPoint))
    unicodeName=unicodedata.name(character,' ')
    return result(character,unicodeName,Num)

def TraductHexa(EntryPoint):
    char=chr(int(EntryPoint[2:], 16))
    number = ord(char)
    character = chr(int(number))
    name_unicode = unicodedata.name(chr(number),' ')
    return result(character,name_unicode,number)

def TraductUnicode(EntryPoint):
    number = ord(EntryPoint)
    character = chr(int(number))
    name_unicode = unicodedata.name(chr(number),' ')
    return result(character,name_unicode,number)

def TraductLetter(EntryPoint):
    i=0
    result=dict()
    for k in range(229999):
        character = chr(k)
        name_unicode = unicodedata.name(character,' ')
        a_bool = EntryPoint in name_unicode
        if(a_bool == True):
            actual=unicodedata.lookup(name_unicode)
            number = ord(actual)
            name_unicode = unicodedata.name(chr(number),' ')
            result[i] = {}   
            result[i]['unicode']=u""+character+""
            result[i]['name']=name_unicode
            result[i]['number']=number
            
            i=i+1
    return result

def UniqueUni(codepoint):
    allInformations=dict()
    character = chr(int(codepoint))
    print(str(chr(int(codepoint))))
    hexauni = hex(ord(character))
    hexauni = hexauni.replace("0x", "U+")
    name_unicode = unicodedata.name(character,' ')
    category = unicodedata.category(chr(int(codepoint)))
    allInformations['unicode']=u""+character+""
    allInformations['hexa']=hexauni 
    allInformations['name']=name_unicode
    allInformations['number']=int(codepoint)
    allInformations['cat']=category
    return allInformations