import pandas as pd
from time import sleep
from datetime import datetime
from os.path import exists

# list of name, degree, score
nme = []
sze = []
tme = []
 # dictionary of lists
data = {'Name': nme, 'Party Size': sze, 'Time': tme}
options = ['new', 'update', 'remove', 'show']
count = 0

df = pd.DataFrame(data) 
def new_data():
    global nme
    global sze
    global tme
    global df
    name = input('Name: ')
    nme.append(name)
    size = input('Size: ')    
    sze.append(size)
    now = datetime.now()
    time = now.strftime("%I:%M:%S")
    tme.append(time)
    df = pd.DataFrame(data)
    #print(df)

def save_data():
    global df
    df.to_csv('waitlist.csv')
    print('Saving Data...')

def load_data():
    print('Loading Data...')
    global df
    df = pd.read_csv('waitlist.csv')
    for item in df['Name'].values.tolist():
        #print(item)
        nme.append(item)
    for item in df['Party Size'].values.tolist():
        #print(item)
        sze.append(item)
    for item in df['Time'].values.tolist():
        #print(item)
        tme.append(item)
        
def show():
    global df
    df = pd.read_csv('waitlist.csv')
    print(df)

def update(x):
    global df
    for item in df['Name'].values.tolist():
        if x in item:
            new_name = input('New Name: ')
            df['Name'] = df['Name'].replace([x], new_name)
            df.to_csv('waitlist.csv')
            print('Updated Name!')
            print(df.index[df[x]].tolist())

#Initialize
if exists('waitlist.csv'):
    load_data()
else:
    df = pd.DataFrame(data)
    df.to_csv('waitlist.csv')

#Main Loop
while count < 1000:
    for item in df['Name'].values.tolist():
        count+=1
    q = input(f'What would you like to do? \n {options}: \n')
    if 'new' in q:
        new_data()
        save_data()
        count+=1
    if 'update' in q:
        name = input('Who would you like to Update?: \n')
        update(name)
    if 'remove' in q:
        pass
    if 'show' in q:
        show()
