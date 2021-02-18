import pandas as pd
import numpy as np
import matplotlib as pl
def main_menu():
  print('\n')
  print(70*'*')
  print('***Read Data Frame File in Different Way***')
  print('1.Read Complete csv File...')
  print('2.Reading complete csv File Without Index...')
  print('3.Reading File With New Column Names...')
  print(50*'=')
  print('*** Data visualization ***')
  print('4.Line Chart...')
  print('5.Bar Chart...')
  print('6.Histogram...')
  print(50*'=')
  print('*** Data Manipulation In The Records Or csv File ***')
  print('7.Sorting The Data As Per Your Choise...')
  print('8.Read Top and Bottom Records From File As Required...')
  print('9.Make a Copy of csv File')
  print('10.Read The Specific Column')
  print('11.Exit...')
  print(70*'*')
  print('\n')
  def readcsv():
      print('Readin Data From csv File...')
      df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv')
      print(df)
  def noIndex():
    print('Reading Data From csv File Without Index Values...')
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv',index_col=0)
    print(df)

  def newcols():
    print('Reading Data From csv File With New Columns Names...')
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv',index_col=0,skiprows=1,names=['eng','Acc','Bst','Eco','IP'])

  def linePlot():
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv')
    stud=df['Student']
    eng=df['English']
    acc=df['Accounts']
    bst=df['B.st']
    eco=df['Economics']
    ip=df['IP']
    pl.xlable('Students')
    pl.xticks(rotation=30)
    print ('Select Specific Line Chart As Given Below : ') 
    print ('Press 1 To Print The Data For student vs English...')
    print ('Press 2 To Print The Data For Students vs Accounts...')
    print ('Press 3 To Print The Data For student vs BSt...')
    print ('Press 4 To Print The Data For Student Economics...')
    print ('Press 5 To Print The Data For Student vs IP...') 
    print ('Press 6 To Merge All the Data In One Chart...')

  op=int(input('enter your choise :'))
  if op==1:
    pl.ylabel('English')
    pl.title('*** Students Marks In English***')
    pl.plot(stud,eng)
    pl.show()
  elif op==2:
    pl.ylabel('Accounts')
    pl.title('***Students Marks In Accounts***')
    pl.plot(stud,acc)
    pl.show()
  elif op==3:
    pl.ylabe1('B.St.')
    pl.title('***students marks in B.St.***')
    pl.plot(stud,bst)
    pl.show()
  elif op==4:
    pl.ylabel('Economics')
    pl.title('***students marks in economics***')
    pl.plot(stud,eco)
    pl.show()
  elif op==5:
    pl.ylabel('ip')
    pl.title('***students marks in ip***')
    pl.plot(stud,ip)
    pl.show()
  elif op==6:
    pl.ylabel('Marks In Subjects')
    pl.title('***Students Marks In Examination**')
    pl.plot(stud,eng,label='Eng')
    pl.plot(stud,acc,label='Acc')
    pl.plot(stud,bst,label='B.St')
    pl.plot(stud,eco,label='Eco')
    pl.plot(stud,ip,label='IP')
    pl.legend()
    pl.show()
  else:
    print('Enter a Valid Input...')
    linePlot()

  def barPlot():
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv')
    stud=df['student']
    eng=df['English']
    acc=df['Accounts']
    bst=df['B.St']
    eco=df['Economics']
    ip=df['IP']
    pl.xlabel('Students')
    pl.xticks(rotation=30)

    print('select specific bar chart as given below :') 
    print('Press 1 To Print The Data For student vs English...')
    print('Press 2 To Print The Data For Students vs Accounts...')
    print('Press 3 To Print The Data For student vs BSt...')
    print('Press 4 To Print The Data For Student Economics...')
    print('Press 5 To Print The Data For Student vs IP...') 
    print('Press 6 To Print All The Data In The Form Of Stack Bar Chart...')
    print('Press 7 To Print All The Data InTHe Form Of Multi Bar Chart...')

    op=int(input('Enter Your Choise :'))

  if op==1:
    pl.ylabel('English')
    pl.title('*** Students Marks In English***')
    pl.bar(stud,eng)
    pl.show()
  elif op==2:
    pl.ylabel('Accounts')
    pl.title('***Students Marks In Accounts***')
    pl.bar(stud,acc)
    pl.show()
  elif op==3:
    pl.ylabe1('B.St.')
    pl.title('***students marks in B.St.***')
    pl.bar(stud,bst)
    pl.show()
  elif op==4:
    pl.ylabel('Economics')
    pl.title('***students marks in economics***')
    pl.bar(stud,eco)
    pl.show()
  elif op==5:
    pl.ylabel('IP')
    pl.title('***students marks in ip***')
    pl.bar(stud,ip)
    pl.show()
  elif op==6:
    pl.ylabel('Marks In Subjects')
    pl.title('***Students Marks In Examination***')
    pl.bar(stud,eng,color='g', width=0.3, label='Eng')
    pl.bar(stud,acc,color='r', width=0.3, label='Acc')
    pl.bar(stud,bst,color='y', width=0.3, label='BSt')
    pl.bar(stud,eco,color='k', width=0.3, label='Eco')
    pl.bar(stud,ip,color='b', width=0.3, label='IP')
    pl.legend()
    pl.show()
  elif op==7:
    l=np.arange(len(stud))
    pl.ylabel('Marks In Subjects')
    pl.title('***Students Marks In Examination***')
    pl.bar(l,eng,color='g', width=0.2, label='Eng')
    pl.bar(l+0.2,acc,color='r',width=0.2, label='Acc')
    pl.bar(l+0.4,bst,color='y',width=0.2, label='BSt')
    pl.bar(l+0.6,eco,color='k',width=0.2, label='Eco')
    pl.bar(l+0.8,ip,color='b',width=0.2, label='IP')
    pl.legend()
    pl.show()
  else:
    print('Enter A Valid Input...')
    barPlot()

  def histogram():
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv')
    eng=df['English']
    acc=df['Accounts']
    bst=df['B.st.']
    eco=df['Economics']
    ip=df['IP']
    mR=[0,10,20,30,40,50,60,70,80,90,100,110]

    print('press 1 To Display Histogram Between Students vs English Marks...')
    print('press 2 To Display Histogram Between Students vs Accounts Marks...')
    print('press 3 To Display Histogram Between Students vs B.st. Marks...')
    print('press 4 To Display Histogram Between Students vs Economics Marks...')
    print('press 5 To Display Histogram Between Students vs IP Marks...')

    op=int(input('Enter your choice:'))
  if op==1:
    pl.title('***Students Marks In English***')
    pl.hist(eng, bins=mR, color='y', rwidth=0.5, label='Eng')
    pl.xticts(mR)
    pl.yticts([0,1,2,3,4])
    pl.xlabel('Marks Range')
    pl.ylabel('No. of students')
    pl.show()
  elif op==2:
    pl.title('***Students Marks In Accounts***')
    pl.hist(acc, bins=mR, color='k', rwidth=0.5, label='Acc')
    pl.xticts(mR)
    pl.yticts([0,1,2,3,4])
    pl.xlabel('Marks Range')
    pl.ylabel('No. of students')
    pl.show()
  elif op==3:
    pl.title('***Students Marks in B.st.***')
    pl.hist(bst, bins=mR, color='g', rwidth=0.5, label='B.st.')
    pl.xticts(mR)
    pl.yticts([0,1,2,3,4])
    pl.xlabel('Marks Range')
    pl.ylabel('No. of students')
    pl.show()
  elif op==4:
    pl.title('***Students Marks in Economics***')
    pl.hist(bst, bins=mR, color='r', rwidth=0.5, label='Eco')
    pl.xticts(mR)
    pl.yticts([0,1,2,3,4])
    pl.xlabel('Marks Range')
    pl.ylabel('No. of students')
    pl.show()
  elif op==5:
    pl.title('***Students Marks in IP***')
    pl.hist(bst, bins=mR, color='b', rwidth=0.5, label='IP')
    pl.xticts(mR)
    pl.yticts([0,1,2,3,4])
    pl.xlabel('Marks Range')
    pl.ylabel('No. of students')
    pl.show()
  else:
    print('Enter a valid Input...')
    histogram()

  def dataSort():
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv')
    print('Press 1 To Arrange The Data As Per English...')
    print('Press 2 To Arrange The Data As Per Accounts...')
    print('Press 3 To Arrange The Data As Per B.st...')
    print('Press 4 To Arrange The Data As Per Econmics...')
    print('Press 5 To Arrange The Data As Per IP...')

    op=int(input('Enter your choice:'))
  if op==1:
    df.sort_values(['English'], inplace=True)
    print(df)
  elif op==2:
    df.sort_values(['Accounts'], inplace=True)
    print(df)
  elif op==3:
    df.sort_values(['B.St'], inplace=True)
    print(df)  
  elif op==4:
    df.sort_values(['Economics'], inplace=True)
    print(df)
  elif op==4:
    df.sort_values(['IP'], inplace=True)
    print(df)
  else:
    print('Enter A Valid Input...')
    dataSort()

  def topBottomSelect():
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv',index_col=0)
    t=int(input('How many Records To Display From Top'))
    print('First',t,'Records...')
    print(df.heas(t))

    b=int(input('How Many Records To Display From Bkottom :'))
    print('Last',b,'Records...')
    print(df.tail(b))

  def duplicate():
    print('Duplicate The File With A New csv File...')
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv')
    df.to_csv('C:\\Users\\sunilgour\\Documents\\stud_data_record.csv')
    print('Data From The New File...')
    print(df)

  def specificCols():
    print('Reading Specific Column From csv File...')
    df=pd.read_csv('C:\\Users\\sunilgour\\Documents\\stud_data.csv',usecols=['student','IP'],index_col=0)
    print(df)

    while True:
      Main_Menu()
      ch=input('Enter Your Choise :')
      if ch=='1':
        readCSV()
      elif ch=='2':
        noIndex()
      elif ch=='3':
        newCols()
      elif ch=='4':
        linePlot()
      elif ch=='5':
        barPlot()
      elif ch=='6':
        histogram()
      elif ch=='7':
        dataSort()
      elif ch=='8':
        topBottomSelect()
      elif ch=='9':
        duplicate()
      elif ch=='10':
        specificCols()
      elif ch=='11':
        break
      else:
        print('\n***Enter A Valid Choise***')


 
