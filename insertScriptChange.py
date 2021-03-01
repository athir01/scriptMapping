with open("/PI/testRead.txt","r") as file:
    text=file.readlines()  #this is a list

i=0
while i < len(text):
    if '[' in text[i]:
        text[i]=text[i].replace('[','')
    i=i+1
    
i=0
while i < len(text):
    if ']' in text[i]:
        text[i]=text[i].replace(']','')
    i=i+1
    
i=0
while i < len(text):
    if 'N\'' in text[i]:
        text[i]=text[i].replace('N\'','\'')
    i=i+1

i=0    
while i < len(text):
    if 'GO' in text[i]:
        text[i]=text[i].replace('GO','bruh')
    i=i+1
    
i=0
while i < len(text):
    if '|' in text[i]:
        text[i]=text[i].replace('|','')
    i=i+1
    
i=0
while i < len(text):
    if '\'TRUE\'' in text[i]:
        text[i]=text[i].replace('\'TRUE\'','true')
    i=i+1
    
i=0
while i < len(text):
    if '\'FALSE\'' in text[i]:
        text[i]=text[i].replace('\'FALSE\'','false')
    i=i+1
    
i=0
while i < len(text):
    if '\\\'' in text[i]:
        text[i]=text[i].replace('\\\'','\'\'')
    i=i+1
    
i=0
while i < len(text):
    if '\\\'' in text[i]:
        text[i]=text[i].replace('\\\'','\'\'')
    i=i+1
    
i=0
while i < len(text):
    if '\')' in text[i]:
        text[i]=text[i].replace('\')','\');')
    i=i+1
    
i=0
while i < len(text):
    if 'NULL' in text[i]:
        text[i]=text[i].replace('NULL','\'\'')
    i=i+1

with open("/PI/testWrite.txt","w") as file1:
    file1.writelines(text)