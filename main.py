import pandas as pd
from time import sleep
from datetime import datetime
from os.path import exists

class MyData:
    nme = []
    sze = []
    tme = []
    # dictionary of lists
    data = {'Name': nme, 'Party Size': sze, 'Time': tme}
    options = ['new', 'update', 'remove', 'show']
    count = 0

    df = pd.DataFrame(data) 
    def __init__(self):
        pass

    def new_data():
        name = input('Name: ')
        MyData.nme.append(name)
        size = input('Size: ')    
        MyData.sze.append(size)
        now = datetime.now()
        time = now.strftime("%I:%M:%S")
        MyData.tme.append(time)
        MyData.df = pd.DataFrame(MyData.data)
        #print(df)

    def save_data():
        MyData.df.to_csv('waitlist.csv', index=False)
        print('Saving Data...')

    def load_data():
        print('Loading Data...')
        MyData.df = pd.read_csv('waitlist.csv')
        for item in MyData.df['Name'].values.tolist():
            #print(item)
            MyData.nme.append(item)
        for item in MyData.df['Party Size'].values.tolist():
            #print(item)
            MyData.sze.append(item)
        for item in MyData.df['Time'].values.tolist():
            #print(item)
            MyData.tme.append(item)
            
    def show():
        MyData.df = pd.read_csv('waitlist.csv')
        print(MyData.df)

    def update(x):
        if x in MyData.df['Name'].values.tolist():
            new_name = input('New Name: ')
            MyData.df['Name'] = MyData.df['Name'].replace([x], new_name)
            print(MyData.df)
            MyData.df.to_csv('waitlist.csv', index=False)
            print('Updated Name!')
            
    def remove(x):
        if x in MyData.df['Name'].values.tolist():
            MyData.df.drop(MyData.df.index[MyData.df['Name'] == x], inplace=True)
            print(MyData.df)
            MyData.df.to_csv('waitlist.csv', index=False)
            print('Removed Name!')
            
#Initialize
if exists('waitlist.csv'):
    MyData.load_data()
else:
    MyData.df = pd.DataFrame(MyData.data)
    MyData.df.to_csv('waitlist.csv')

#Main Loop
while True:
    q = input(f'What would you like to do? \n {MyData.options}: \n')
    if 'new' in q:
        MyData.new_data()
        MyData.save_data()
    if 'update' in q:
        name = input('Who would you like to Update?: \n')
        MyData.update(name)
    if 'remove' in q:
        name = input('Who would you like to Remove?: \n')
        MyData.remove(name)
    if 'show' in q:
        MyData.show()
