class Person:
    """
    A class to represent a person.

    Attributes:
        name(str): name of the person
        age(int): age of the person


    Methods:
        info(): Prints the person's name and age.
    """

    def __init__(self, name, age):
        """
        Constructs all the necessary attributes for the person object.

        Arguments:
            name(str): name of the person
            age(int): age of the person

        Returns: 
            None
        """

        self.name = name
        self.age = age

    def info(self):
        """
        Prints the person's name and age.

        Arguments:


        Returns: 
            None
        """

        print(f"My name is {self.name}. I am {self.age} years old.")


Person("John", 24).info()  # My name is John. I am 24 years old.
