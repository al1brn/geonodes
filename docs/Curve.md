
# Class Curve

Instances inherits both from DataSocket and from Domain
class Instances(Domain):

  def init_socket(self):
    super().init_socket()
    self.domain = 'INSTANCES'
    
    
    