class secondLargest:
  
  def __init__(self,lst):
    self.lst=lst
  
  def sortList(self):
    dlst=list(set(self.lst))
    for i in range(len(dlst)):
      for k in range(i+1):
        if dlst[k] < dlst[i]:
          dlst[i] , dlst[k] = dlst[k] , dlst[i]
          
    return dlst[1]
  
  def getNumber(self):
    n=self.sortList()
    return f"The second largest number is {n} "
  
  

l=[4,5,3,6,2,8,7,8,6,9,4,5]
second=secondLargest(l)
print(second.getNumber())
  
