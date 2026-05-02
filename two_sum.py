class TwoSum:
  
  def __init__(self,lst,target):
    self.lst=lst
    self.target=target
  
  def get_inices(self):
    lookup={}
    ind=[]
    
    for i,num in enumerate(self.lst):
      complement=self.target - num
      
      if complement in lookup:
        ind.extend([lookup[complement], i])
      
      lookup[num]=i
    
    return ind
      
    
      
      
      
num=[3, 5, 7, 4, 1, 2]
target=6
sm=TwoSum(num,target)
print(sm.get_inices())