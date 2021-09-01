#creating linked lists in Python

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval


l1 = SLinkedList()
l1.headval = Node(10)
l2 = Node(20)
l3 = Node(30)
l1.headval.nextval = l2
l2.nextval = l3

l1.listprint()