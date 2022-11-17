import pandas as pd
from time import sleep
from datetime import datetime
from os.path import exists
import tkinter as tk

class MyData:
    nme = []
    sze = []
    tme = []
    sts = []
    # dictionary of lists
    data = {'Name': nme, 'Party Size': sze, 'Time': tme, 'Status': sts}
    options = ['new', 'update', 'remove', 'show', 'seat']

    df = pd.DataFrame(data) 
 
    def __init__(self):
        return

    def new_data():
        print(f'{MyData.nme}, {MyData.sze}, {MyData.tme}, {MyData.sts},')
        name = input('Name: ')
        MyData.nme.append(name)
        size = input('Size: ')    
        MyData.sze.append(size)
        now = datetime.now()
        time = now.strftime("%I:%M:%S")
        MyData.tme.append(time)
        status = "waiting"
        MyData.sts.append(status)
        MyData.df = pd.DataFrame(MyData.data)
        MyData.save_data()
        #print(df)

    def save_data():
        MyData.df.to_csv('waitlist.csv', index=0)
        print('Saving Data...')
        MyData.show()

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
        for item in MyData.df['Status'].values.tolist():
            #print(item)
            MyData.sts.append(item)
        print(MyData.df)
        
    def seat(x):
        temp = MyData.df['Name'].values.tolist()
        index = temp.index(x)
        #print(index)
        #print(temp)
        del MyData.nme[index]
        del MyData.sze[index]
        del MyData.tme[index]
        del MyData.sts[index]
        new_status = input(f'Would you Like to Seat {x}? (y/n): ')
        if 'y' in new_status:
            if x in MyData.df['Name'].values.tolist():
                MyData.df.loc[index:index,'Status'] = 'Completed'
                #MyData.df.drop(MyData.df.index[MyData.df['Name'] == x], inplace=True)
                MyData.df.to_csv('waitlist.csv', index=False)
                print('Customer Updated!')
                MyData.show()        
        else:
            pass
            
    def show():
        MyData.df = pd.read_csv('waitlist.csv')
        print(MyData.df[MyData.df.Status == 'waiting'])
    
    def show_completed():
        MyData.df = pd.read_csv('waitlist.csv')
        print(MyData.df[MyData.df.Status == 'Completed'])
    
    def show_all():
        MyData.df = pd.read_csv('waitlist.csv')
        print(MyData.df)

    def update_name(x):
        if x in MyData.df['Name'].values.tolist():
            new_name = input('New Name: ')
            MyData.df['Name'] = MyData.df['Name'].replace([x], new_name)
            print(MyData.df)
            MyData.df.to_csv('waitlist.csv', index=0)
            print('Updated Name!')
            MyData.show()
    
    def update_size(x):
        temp = MyData.df['Name'].values.tolist()
        index = temp.index(x)
        new_size = input('New Party Size: ')
        MyData.df.loc[index:index,'Party Size'] = new_size
        MyData.df.to_csv('waitlist.csv', index=False)
        print('Updated Party Size!')
        MyData.show()

            
    def remove(x):
        temp = MyData.df['Name'].values.tolist()
        index = temp.index(x)
        #print(index)
        #print(temp)
        del MyData.nme[index]
        del MyData.sze[index]
        del MyData.tme[index]
        del MyData.sts[index]
        if x in temp:
            MyData.df.drop(MyData.df.index[MyData.df['Name'] == x], inplace=True)
            print(MyData.df)
            MyData.save_data()
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
    elif 'update' in q:
        what = input('What would you like to update?: \n name, size: ')
        if 'size' in what:
            MyData.show()
            name = input('Name of Party: ')
            MyData.update_size(name)
        elif 'name' in what:
            MyData.show()
            name = input('Who would you like to Update?: \n')
            MyData.update_name(name)
    elif 'remove' in q:
        name = input('Who would you like to Remove?: \n')
        MyData.remove(name)
    elif 'show' == q:
        MyData.show()
    elif 'show_completed' == q:
        MyData.show_completed()
    elif 'show_all' == q:
        MyData.show_all()
    elif 'seat' == q:
        MyData.show()
        name = input('Name of Party: ')
        MyData.seat(name)