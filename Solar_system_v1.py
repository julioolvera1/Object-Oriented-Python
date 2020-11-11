### Solar system
import numpy as np

class CelestialBody:

    def __init__(self,name,radius,mass,temperature):

        self.name=name
        self.radius=radius
        self.mass=mass
        self.temperature=temperature

    
class Star(CelestialBody):

    @property
    def power(self):
        power = 4*np.pi*5.7e-8*self.radius**2*self.temperature**4
        print(f'Power of star {self.name} is: {power/1e24:.2f} YW')
        return(power)

    
class Planet(CelestialBody):

    def __init__(self,name,radius,mass,temperature,distance_from_star):
        super().__init__(name,radius,mass,temperature)

        self.distance_from_star=distance_from_star

    @property
    def orbital_period(self):
        # We can use the mass of the star instance variable
        period=2 * np.pi * np.sqrt(self.distance_from_star ** 3 / (6.6726e-11 * self.star.mass))
        print(f'Orbital period of {self.name}: {period:.2f} seconds')
        print(f'Orbital period of {self.name}: {period*3.17098e-8:.2f} years')
        return(period)

class RockyPlanet(Planet):

    def __init__(self, name, radius, mass, temperature, distance_from_star,surface_pressure):
        super().__init__(name, radius, mass, temperature, distance_from_star)

        self.surface_pressure = surface_pressure


class GasPlanet(Planet):
    def __init__(self, name, radius, mass, temperature, distance_from_star,methane_perc):
        super().__init__(name, radius, mass, temperature, distance_from_star)

        self.methane_perc=methane_perc

class SolarSystem:

    def __init__(self,star):
        self.star=star
        self.planets=[]


        self.planets_names = []
    
    def add_planet(self,planet):
        # When we add a planet, also set a reference to the star of the solar system
        # so that the mass of the star can be used as instance variable
        planet.star=self.star
        self.planets.append(planet)
        self.planets_names.append(planet.name)

    def __str__(self):

        return(f'Solar system with star {self.star.name} and planets {self.planets_names}')


star_1 = Star('Sun', radius=7e8, mass=2e30, temperature=5778)
star_1.power

solar_system_1 = SolarSystem(star=star_1)
print(solar_system_1)

planet_1 = RockyPlanet(name='Earth', radius=6.4e6, mass=6e24, temperature=288, distance_from_star=1.5e11, surface_pressure=1e5)

solar_system_1.add_planet(planet_1)
print(solar_system_1)

planet_2 = GasPlanet("Jupiter", 7e7, 1.9e27, 128, 7.7e11, 0.3)

planet_3=GasPlanet("Uranus", 2.5e8, 8.7e25, 49, 3e12, 2.3)

solar_system_1.add_planet(planet_2)
solar_system_1.add_planet(planet_3)

print(solar_system_1)


planet_1.orbital_period
planet_2.orbital_period
planet_3.orbital_period






