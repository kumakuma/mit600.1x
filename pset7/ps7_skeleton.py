import random as rand
import string
import math

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location_x = float(location[0])
        self.location_y = float(location[1])

    def get_number_of_species(self, animal):
        if animal in self.species_types:
            return self.species_types[animal]
        else:
            return 0

    def get_location(self):
        return (self.location_x, self.location_y)

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        if species in self.species_types:
            num = self.get_number_of_species(species)
            if num <= 1:
                del self.species_types[species]
            elif num > 1:
                self.species_types[species] -= 1


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.get_desired_species())
        return float(1 * num_desired)


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center)
        num_other = 0
        for species in self.considered_species:
            num_other += adoption_center.get_number_of_species(species)
        score += 0.3 * num_other

        return float(score)


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)

        num_feared = adoption_center.get_number_of_species(self.feared_species)

        score = float(adopter_score - (num_feared * 0.3))
        if score < 0:
            return 0.0

        else:
            return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):

        for species in self.allergic_species:
            if adoption_center.get_number_of_species(species):
                return 0.0

        return Adopter.get_score(self, adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medication_effectiveness):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        self.medication_effectiveness = medication_effectiveness

    def get_score(self, adoption_center):
        lowest_effectiveness = 1.0
        for species in self.allergic_species:
            if adoption_center.get_number_of_species(species):
                if species in self.medication_effectiveness:
                    effectiveness = self.medication_effectiveness[species]
                    if effectiveness < lowest_effectiveness:
                        lowest_effectiveness = self.medication_effectiveness[species]

        return Adopter.get_score(self, adoption_center) * lowest_effectiveness

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        x = self.location[0]
        y = self.location[1]

        ac_x = to_location[0]
        ac_y = to_location[1]

        distance = math.sqrt((x - ac_x) ** 2 + (y - ac_y) ** 2)

        return float(distance)

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance < 1:
            return adopter_score
        elif 1 <= distance < 3:
            return rand.uniform(0.7, 0.9) * adopter_score
        elif 3 <= distance < 5:
            return rand.uniform(0.5, 0.7) * adopter_score
        else:
            return rand.uniform(0.1, 0.5) * adopter_score


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    def get_scores(item):
        return adopter.get_score(item)

    def get_string(item):
        return item.get_name().lower()

    list_of_adoption_centers.sort(key=get_string)
    list_of_adoption_centers.sort(key=get_scores, reverse=True)
    #
    # for i in list_of_adoption_centers:
    #     print (i.get_name(), adopter.get_score(i))

    return list_of_adoption_centers

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """

    def get_scores(elem):
        return elem.get_score(adoption_center)

    def get_string(item):
        return item.get_name().lower()

    list_of_adopters.sort(key=get_string)
    list_of_adopters.sort(key=get_scores, reverse=True)
    result = []

    num_adopters = len(list_of_adopters)

    iterations = min(num_adopters, n)

    for i in range(iterations):
        result.append(list_of_adopters[i])

    return result

