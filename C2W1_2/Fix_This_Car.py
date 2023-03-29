#!/usr/bin/env python
# coding: utf-8

# # Clean up test code lab
# 
# The goal for this lab is for you the student to learn how to write 
# good unit tests by cleaning them up some bad ones. The first cell contains 
# class ``Car`` which is the class we'll be testing. Look at the code
# so that you'll make sense of it, no need to actually modify it.
# The second second cell contains a class called ``TestCar`` which
# tests all of methods of ```Car.``` There's a couple issues though,
# none of the unit tests in ```TestCar``` pass for one, and some of them
# are not designed using good unit testing practices. 
# 
# 
# ## Instructions for the Lab
# 
# Here's the instructions for the lab:
# 
# - ```test_default```: Let's refactor the name to be more descriptive, 
# right now it's not very expressive. Once done, fix the testing
# logic so it actually passes!
# - ```test_change```: Again, this unit test is poorly name. Refactor it
# so that it's name gives the meaning behind it. Once done, fix the
# logic so that the it passes.  
# - ```test_current_speed```: Alas, this unit test is named nicely, but there's
# something terribly wrong with the unit test. What is it? Make the update.
# - ```test_accelerate```: This unit test violates one of the principles
# for developing good unit tests. Refactor it so that it's clean and
# does one job and one job only.
# - ```test_brake```: This unit test doesn't pass, fix it so that it does. 

# In[1]:


class Car:
    """
    Setup the default state of car object
    """

    def __init__(self):
        self.speed = 0              # default speed
        self.MAX = 120              # max speed
        self.BREAK_AMOUNT = 10      # break amount in mph
        self.color_options = {      # color options for the car
            1: 'black',
            2: 'green',
            3: 'orange',
            4: 'white',
            5: 'pink'
        }

        self.current_color = self.color_options[1]

    def __repr__(self):
        """
        Create a string representation of car object
        :return: current speed and color
        """
        return f'Speed: {self.speed} Color: {self.current_color}'

    def change_color(self, option) -> str:
        """
        changes color of car, choose values 1-5
        :param option: the new color of the car
        :return: the current color of car
        """
        try:
            if 1 <= option <= 5:
                if self.current_color == self.color_options[option]:
                    return self.current_color
                else:
                    self.current_color = self.color_options[option]
                    return self.current_color
        except TypeError:
            print('Ints: 1-5')

    def accelerate(self, velocity, max=120) -> int:
        """
        increase speed of car
        :param velocity: speed up amount
        :param max: limit to speed increase
        :return:  current speed
        """
        try:
            if self.speed < self.MAX and velocity > 0:
                self.speed += velocity
        except ValueError:
            print(f'self.speed or velocity are invalid. Your values: {velocity}, or {self.speed}')
        return self.speed

    def brake(self, velocity) -> int:
        """
        decelerate your car
        :param velocity: rate of slow down
        :return: current speed
        """
        try:
            if self.speed - velocity < 0 or velocity > self.BREAK_AMOUNT:
                raise ValueError
            else:
                self.speed -= velocity
                return self.speed
        except ValueError:
            print('invalid')


# In[2]:



        
import unittest


class TestCar(unittest.TestCase):
        
    def test_default_color(self):
        self.c1 = Car()
        self.assertEqual(self.c1.current_color, 'black')
    
    def test_change_color(self):
        self.c1 = Car()
        self.assertEqual(self.c1.change_color(3), 'orange')
    
    def test_current_speed(self):
        self.c1 = Car()
        self.assertAlmostEqual(self.c1.speed, 0)
    
    
    def test_accelerate(self):
        self.c1 = Car()
        self.c1.accelerate(20)
        self.assertEqual(self.c1.speed, 20)
        
    
    def test_brake(self):
        self.c1 = Car()
        self.c1.accelerate(20)
        self.c1.brake(5)
        self.assertEqual(self.c1.speed, 15)
    

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
        

