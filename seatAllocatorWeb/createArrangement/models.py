from django.db import models

# Create your models here.
class classRooms(models.Model):
    noOfRooms=models.CharField(max_length=10, default=" ",blank=True,null=True)
    room1 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room2 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room3 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room4 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room5 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room6 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room7 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room8 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room9 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    room10 = models.CharField(max_length=1000, default=" ",blank=True,null=True)

    def __str__(self):
        return str(self.noOfRooms) + ' ' + str(self.room1) + ' ' + str(self.room2) + ' ' + str(self.room3)+ ' ' + str(self.room4) + ' ' + str(self.room5)+ ' ' + str(self.room6) + ' ' + str(self.room7) + ' ' + str(self.room8)+ ' ' + str(self.room9) + ' ' + str(self.room10)

    """rows = models.CharField(max_length=2, default=" ")
    cols = models.CharField(max_length=2, default=" ")
    roomid=models.CharField(max_length=10,default=" ")
    def __str__(self):
        return self.noOfRooms + ' ' + self.rows + ' ' + self.cols + ' ' + self.roomid"""

class deptAndSec(models.Model):
    noOfDepts = models.CharField(max_length=3, default=" ")
    section1=models.CharField(max_length=1000,default=" ",blank=True,null=True)
    section2 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section3 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section4 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section5 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section6 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section7 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section8 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section9 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    section10 = models.CharField(max_length=1000, default=" ",blank=True,null=True)
    def __str__(self):
        return str(self.noOfDepts) + ' ' + str(self.section1) + ' ' + str(self.section2) + ' ' + str(self.section3)+ ' ' + str(self.section4) + ' ' + str(self.section5)+ ' ' + str(self.section6) + ' ' + str(self.section7) + ' ' + str(self.section8)+ ' ' + str(self.section9) + ' ' + str(self.section10)


    """nameOfDept=models.CharField(max_length=20,default=" ")
    sectionsInDept=models.CharField(max_length=4,default=" ")
    secName=models.CharField(max_length=8,default=" ")
    secCapacity=models.CharField(max_length=8,default=" ")
    startingRoll=models.CharField(max_length=15,default=" ")
    endingRoll=models.CharField(max_length=15,default=" ")
    def __str__(self):
        return self.noOfDepts + ' ' + self.nameOfDept + ' ' + self.sectionsInDept+ ' ' + self.secName + ' ' + self.secCapacity+ ' '+self.startingRoll+' '+self.endingRoll"""


class addAndDel(models.Model):
    addNum = models.CharField(max_length=1000,default=" ",blank=True,null=True)
    addNumRoll = models.CharField(max_length=1000,default=" ",blank=True,null=True)
    delNum = models.CharField(max_length=1000,default=" ",blank=True,null=True)
    delNumRoll = models.CharField(max_length=1000,default=" ",blank=True,null=True)
    def __str__(self):
        return str(self.addNum) + ' ' + str(self.addNumRoll) + ' ' + str(self.delNum) + ' ' + str(self.delNumRoll)
