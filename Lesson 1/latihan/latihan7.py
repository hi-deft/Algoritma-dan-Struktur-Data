staff = { 
    'Santi': 'santi@ums.ac.id', 
    'Jokovi': 'jokovi@solokao.go.id', 
    'Endang': 'Endang@yahoo.com', 
    'Sulastri': 'Sulastrii39@gmail.com' 
}

yangDicari = 'Santi'
if yangDicari in staff:
    print('Emailnya', yangDicari, 'adalah', staff[yangDicari])
else:
    print('Tidak ada yang namanya', yangDicari)