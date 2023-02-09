def write_file(data):
    with open('homeTask08/file.csv','a') as file:
        file.writelines(data)
          
def read_file():
    with open('homeTask08/file.csv','r') as file:
        return file.readlines()