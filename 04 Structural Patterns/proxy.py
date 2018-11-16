import time

class Producer:
    """Define the 'resource-intensive' object to instantiate!"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is avaible"""
        print("Artist cheking if producer ia avaible ...")

        if self.occupied == 'No':
            #if the producer is avaible, create a producer object!
            self.producer = Producer()
            time.sleep(2)
            #Make the producer meet the guest!
            self.producer.meet()
            
        else:
            #otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


#Instantiate a proxy
p = Proxy()
#Make the proxy: Artist produce until producer is available
p.produce()
#Change the state to 'occupied'
p.occupied = 'Yes'
#Make the producer produce
p.produce()
    
