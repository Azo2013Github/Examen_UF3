__author__ = 'Amine Banks'

class getWrite:
    contains = True
    app1='Free',
    app2 = 'pay'
    price = '10'
    download = ''
    punctuation = ''
    comment = ''
    objects = ['appli free','App Store','16-05-2014','Price','download', 'number Punctuation', 'Punctuation', 'Number comment']
    def __init__(self, contains):
        self.contains=contains
    def setContains(self, contains):
        self.contains = contains
    def getObjects(self):
        return self.objects
    #write in the file if is application free
    def write(self):
        with open('file2.txt', mode='w', encoding='utf-8') as archive:
            for i in self.getObjects():
                archive.write(i +"\n")
    def getApp1(self):
        return self.app1
    def getApp2(self):
        return self.app2
    def getComment(self):
        return self.comment
    def getDownload(self):
        return self.download
    def getPrice(self):
        return self.price
    def getPunctuation(self):
        return self.punctuation

    #cheching of is the app free
    def cheching(self):
        if(self.contains == False):
            with open('file2.txt', mode='r', encoding='utf-8') as archive:
                for i in archive:
                    print(i[0]+" " +self.getApp2())
        else:
            self.contains = False
            print(self.getApp1())

    def cheching2(self):
        if(self.contains==True):
            with open('file2.txt', mode='r',encoding='uft-8') as archive:
                for i in archive:
                    print(i)
        else:
            print(self.getApp2(), self.getPrice())

# add a new application in the list#
    print("Add a new Application in the list")
    def addApplication(self):
        print("add a new application in the")
        with open('file2.txt', mode='a', encoding='utf-8') as archive:
            archive.write("Tetris")


    # this function is the read the contains of the file:#
    print("print the contains of the file: ")
    def listApplication(self):
        with open('file2.txt', mode='r', encoding='utf-8') as file:
            for i in file:
                print(i)







a = getWrite('file2.txt')
a.write()
a.cheching()
a.cheching2()
a.addApplication()
a.listApplication()