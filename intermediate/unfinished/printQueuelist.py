""" You need to create a class called PrintQUeueList that has an add function protected by two assertions 
 to verify if the new_queue argument is already in the _list array. How do you do this?
 """
class PrintQUeueList:
  def __init__(self):
    self._list = []

  def add(self, new_queue):
    assert new_queue not in self._list, "%r is already in %r" % (self,new_queue)
    assert isinstance(new_queue, PrintQUeueList), "%r is not a print queue" % new_queue