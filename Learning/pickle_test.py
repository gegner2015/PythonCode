import pickle

mylist=[123,1.14,'小哥哥','小姐姐',[5,6,7],{1:'one',2:'two'}]

print(mylist)

pickle_file=open('mylist.pkl','wb')


pickle.dump(mylist,pickle_file)

pickle_file.close()

mylist2=[]

pickle_file_new=open('mylist.pkl','rb')

mylist2=pickle.load(pickle_file_new)

print(mylist2)

pickle_file_new.close()




