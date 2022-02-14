import csv
class Base:
    def write(self):
        with open('imagedetails.csv', 'w') as file:
            writer1 = csv.writer(file)
            writer1.writerow(["SN","filename", "filesize", "image res","image name","no.of .objects","obj res"])
            writer1.writerow([1, "image", "120mb", "123pix","abcd","234","12"])
class Derived(Base):
    def read(self):

         with open('C:\csvfiles\imagedetails.csv', 'r') as file1:
             data=csv.reader(file1)
             for row in data:
                 print(row)
obj=Derived()
obj.write()
obj.read()

