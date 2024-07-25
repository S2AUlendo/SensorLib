# The Instrument class represents a generic musical instrument.
class Instrument:

# The __init__ method accepts an argument for the name of the instrument.
    def __init__(self, name):
        self.__name = name

# The show_name method displays the instrument name. 
    def show_name(self):
        print('I am a', self.__name)

# The make_sound method describes the instrument's sound.
    def make_sound(self):
        print('Lalalala')

# The Guitar class is a subclass of the Instrument class.
class Guitar(Instrument):

# The __init__ method calls the superclass's
# __init__ method passing 'Guitar' as the species.

    def __init__(self):
        Instrument.__init__(self, 'Guitar')

# The make_sound method overrides the superclass's
# make_sound method.
    def make_sound(self):
        print('Strumming Strings')

class Drum_Set(Guitar):

# The __init__ method calls the superclass's
# __init__ method passing 'Drum_Set' as the species.
    def __init__(self):
        Guitar.__init__(self, 'Drum Set')

# The make_sound method overrides the superclass's
# make_sound method.
    def make_sound(self):
        print('Bang, Bang!')        

def main():
    # Create Guitar and a Drums objects.
    guitar = Guitar()
    drums = Drum_Set()

    # Display information about each one.
    print('Here are some instruments and the types of sounds they make.')
    print()
    show_sounds(guitar)
    print()
    show_sounds(drums)
    
 # The show_sounds function accepts an object
 # as an argument, and calls its show_name
 # and make_sound methods.

def show_sounds(instrument_type):
    instrument_type.show_name()
    instrument_type.make_sound()

# Call the main function.
main()