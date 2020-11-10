class Temperature:

    # def __init__(self,temperature):

    #     self.temperature=temperature

    @property
    def celsius(self):
        print(f'Temperature: {self._temperature:.2f} C')
        return self._temperature

    @property
    def farenheit(self):

        farenheit=1.8*self._temperature +32

        print(f'Temperature: {farenheit:.2f} F')
        return (farenheit)

    @celsius.setter  # This is how you set a different value
    def celsius(self, value):

        if value < -273.15:
            raise ValueError('Temperature below absolute zero')

        self._temperature=value
        
    @farenheit.setter
    def farenheit(self,value):

        self.celsius=(value-32)/1.8


temperature_1=Temperature()
temperature_1.celsius=40
temperature_1.celsius
temperature_1.farenheit
temperature_1.farenheit = 0
temperature_1.celsius
temperature_1.farenheit




