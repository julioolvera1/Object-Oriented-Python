## Droplets


class Droplet():

    def __init__(self,ID,volume):

        self.ID=ID
        self.volume=volume
        

    def get_radius(self):

        self.radius=(3*self.volume/4)**(1/3)

    def __str__(self):

        return(f'Droplet ID: {self.ID} with volume: {self.volume:.2f} and radius: {self.radius:.2f} ')

    def __add__(self, other):

        return(Droplet(self.ID+other.ID,self.volume+other.volume))

    def __gt__(self,other):

        if self.volume > other.volume:

            print(f'{self.ID} greater than {other.ID}')
        else:
            print('Not true')

        return(self.volume > other.volume)

    def __lt__(self, other):

        if self.volume < other.volume:

            print(f'{self.ID} smaller than {other.ID}')
        else:
            print('Not true')

        return(self.volume < other.volume)


droplet_1=Droplet('A',1)
droplet_2 = Droplet('B', 2)

droplet_1 > droplet_2
droplet_1 < droplet_2

droplet_1.get_radius()
droplet_2.get_radius()


print(droplet_1)
print(droplet_2)

droplet_3=droplet_1+droplet_2
droplet_3.get_radius()
print(droplet_3)






