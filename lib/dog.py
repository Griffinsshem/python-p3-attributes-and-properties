#!/usr/bin/env python3

class Dog:
    APPROVED_BREEDS = ["Beagle", "Poodle", "Labrador", "German Shepherd", "Bulldog", "Pug"]

    def __init__(self, name="Fido", breed="Beagle"):
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

        if breed not in Dog.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed
