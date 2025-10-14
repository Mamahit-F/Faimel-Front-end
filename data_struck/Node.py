class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None
# Print the linked list
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def AtBegining(self,newdata):
      NewNode = Node(newdata)

# Update the new nodes next val to existing node
      NewNode.nextval = self.headval
      self.headval = NewNode

list = SLinkedList()
list.headval = Node("Informatika")
e2 = Node("Fakultas ilmu komputer")
e3 = Node("Universitas Klabat")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Program studi")
list.listprint()
