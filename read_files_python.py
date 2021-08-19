#open an existing file in your current working directory
my_file = open("dna.txt")

#read the contents.
my_dna = my_file.read()
#the my_dna object is a string object that can be printed
print(my_dna)
#only problem is that python adds the newline character <\n> to strings in text files
#need to remove the <\n> as follows
my_dna = my_dna.rstrip("\n")

#strings in text files can be read in and stripped of the <\n> in one go
my_dna = my_file.read().rstrip("\n")

######## Create files ########

#Create a writeable file in your cwd
#Note that since you are now creating a file it need not exist in your cwd
#Can use the "w" (write) or "a" (append) argument
my_dna = open("out.txt", "w")
my_dna.write("actgtatatc")
#MUST CLOSE FILE FOR IT TO WRITE TO THE HARD DRIVE
my_dna.close()


######## os and shutil modules ########
#get cwd
import os
os.getcwd()
#see files in a given directory
os.listdir()
#rename a file 'out.txt' to 'new.txt'
#to move the file simply add the path in front of 'new.txt'
os.rename("out.txt", "new.txt")
#rename folder
os.rename('/Users/RobertPyne1/PycharmProjects/pythonProject1','/Users/RobertPyne1/PycharmProjects/Code_Academy_worth_saving')

#make a new folder
os.mkdir('Users/RobertPyne1/PycharmProjects/new_folder)
#make a new directory with multiple folders
os.mkdirs('Users/RobertPyne1/PycharmProjects/new_folder1/new_folder2)
#delete a file
os.remove('Users/RobertPyne1/PycharmProjects/new_folder/file.txt')
#delete a directory or folder
os.rmdir('Users/RobertPyne1/PycharmProjects/new_folder/')



#Invoke the shutil function
import shutil
#Make a copy of a file
shutil.copy('/Users/RobertPyne1/PycharmProjects/Code_Academy_worth_saving/new.txt','/Users/RobertPyne1/PycharmProjects/Code_Academy_worth_saving/copy.txt')


