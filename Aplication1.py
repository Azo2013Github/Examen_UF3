__author__ = 'Amine Banks'

class getWrite:
    contains = True
    app1='Free',
    app2 = 'pay'
    price = '10'
    download = ''
    punctuation = ''
    comment = ''
    objects = ['appli free','Google Play Store','16-05-2014','Price: 0','download: 100', 'number Punctuation: 100', 'Punctuation', 'Number comment: 10']
    objects2 =['appli pay', 'App Store','16-05-2014','Price = 10','download = 20', 'number Punctuation: 20', 'Punctuation', 'Number comment: 0']
    def __init__(self, contains):
        self.contains=contains
    def setContains(self, contains):
        self.contains = contains
    def getObjects(self):
        return self.objects
    def getObjects2(self):
        return self.objects2
    #write in the file if is application free
    def write(self):
        with open('file.txt', mode='w', encoding='utf-8') as archive:
            for i in self.getObjects():
                 for line in self.getObjects2():
                    archive.write(line +"\n")

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
    def cheching(self, app):
        d = 'hewu'

    def cheching(self):
        if(self.contains == False):
            with open('file.txt', mode='r', encoding='utf-8') as archive:
                for i in archive:
                    print(i[0]+" " +self.getApp2())
        else:
            self.contains = False
            print(self.getApp1())

    def cheching2(self):
        if(self.contains==True):
            with open('file.txt', mode='r',encoding='uft-8') as archive:
                for i in archive:
                    print(i)
        else:
            print(self.getApp2(), self.getPrice())

# add a new application in the list#
    print("Add a new Application in the list")
    def addApplication(self):
        print("add a new application in the")
        with open('file.txt', mode='a', encoding='utf-8') as archive:
            archive.write("candy crash")

    print("list the contains file in the program:")
    def listApplication(self):
        with open('file.txt', mode='r', encoding='utf-8') as file:
            for i in file:
                print(i)

    #function the modifie data in the for a identification:

    def modifiIdentification(self, nombre, proveedor, fecha):
        with open('file.txt', mode='r', encoding='uff-8') as archivo:
            for i in archivo:
                if self.getObjects()[0].split(','):
                    print(self.getObjects()[0].remove)

    def sumDownload(self):
        suma = self.getDownload() + self.getDownload()
        print(suma)



a = getWrite('file.txt')
#a.write()
#a.cheching()
#a.cheching2()
#a.addApplication()
#a.listApplication()
#a.modifiIdentification()
a.sumDownload()




