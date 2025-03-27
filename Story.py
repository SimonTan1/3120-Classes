from Inventory import Inventory
from Person import Person
class Story:

    def __init__(self):
        self.character = Person()
        self.inventory = Inventory()



    def __init__(self):
        self.survival_pts = 0

    def intro(self):
        print("Ah, there you are. Welcome, dear observer. The desert stretches before us like a parchment yet to be scorched by truth. "
            "Five souls walk its brittle skin and into a labyrinth of darkness, and you—yes, "
            "you above all—will be the author of their fates.")
        print("The sun hangs low, casting long fingers of orange across canvas tents and steel crates. "
              "A lonely wind runs through the dig site—dry, warm, and blasting sand against every surface,")
        print("Beyond the wire fences and excavated trenches lies the entrance: a carved stone arch protruding from the earth, "
            "weathered but defiant—awaiting its next procession of trespassers.")
        print("Dr. Elijah Morrow, a once respected archaeologist, whilst wallowing in failure, "
              "was approached by Aeternum Holdings offered funding, resources, and a promise of fame."
              "And so Elijah stands there, sponsored by corporate suits who brought you here and staffed the "
              "expedition with a crew to investigate a newly uncovered structure, they had "
              "excavated in their surveying efforts on the land for its bountiful resources")
    def beginning_story(self):
        print("Ahead, the carved arch looms—partially unearthed, its surface etched with symbols that "
              "shimmer in the sun like oil on water. Cleopatra’s tomb…")
        print("Leila - the local liaison and desert guide approaches, 'the storm's coming tonight and we are about to finish setting up the generators for the camp' ")
        print("Elijah - 'if the storm arrives tonight we we need to wait a few days before we can start the expedition,"
              "since that is the case, we should make a quick cursory examination of the ruins to study while we wait out the storm")
        print("Jonas - 'love it, i have my camera ready now")
        print("The team enters into the temple, as they walk down the corridor the walls covered in symbols"
              "seem familiar as elijah attempts to decipher the message etched on the walls")
        self.character.add_intel(1)

        print("the team come across a chamber, within the chamber there is a bejeweled dagger at the altar,"
              "it looks like some sort of ceremonial piece, it looks important")
        ch1 = input("what do you do?\n"
                    "1. take video of it, avoid distrubing the artifact \n"
                    "2. take the dagger from the altar \n"
                    
                    "Enter choice (1, 2): ")

        if ch1 == '1':
            print("Jonas moves with Elijah towards the altar and begins recording the setting, the "
                  "dagger looked like it was crusted with dirt and millennia of debris, but staring at it "
                  "Elijah could almost feel as though it was calling him to hold it.")
            self.character.sanity(2)
        elif ch1 == '2':
            print("Elijah grabs the dagger and the debris encrusting the dagger seemed to just fall away,"
                  " the daggers handle was revealed to be lined with precious gems and the blade had symbols "
                  "engraved on it, elijah studies the blade more intently.")
            print("Elijah - 'these glyphs are...wrong, i feel like i know them and recognize there meaning but i "
                  "don't remember learning them.'")
            self.character.add_intel(5)
            self.character.sanity(10)
            self.inventory.inventory_status('ceremonial dagger', True)

        print("the team continues onward to another long corridor, leading to an opening")
        print("the new room was circular in shape with a large cavernous hole on the floor,"
              "Leila approached the edge of the hole and shined he light down")
        print("Leila - 'it doesnt look that deep i can see the bottom, we should be able to get down there if "
              "we tie a rope around one of the surrounding statues and lower ourselves down'")
        print("Elijah - 'we only came in here to get some footage to study while we wait out the storm, we"
              "didn't bring much of anything in the way of supplies and the rest of the camp probably don't know we "
              "are here at all'")
        print("leila - 'i know, but if we dont do thing it could be a week before we can make it back in here "
              "we can just take a quick peek down there and we'll be back out'")
        print("Leila is already beginning to tie the rope to a statue")
        self.inventory.inventory_status('rope', False)
        ch2 = input("what do you do?\n"
                    "1. Don't take the risk, begin to head back to camp \n"
                    "2. Tie a rope and rappel down \n"

                    "Enter choice (1, 2): ")

        if ch2 == '1':
            print("A shrill runs through the ruins, its sound carries with it the obvious indication of danger"
                  "the team shines their lights at the entrance, looking to see who or what had made such a sound")
            self.character.stress(1)
            print("a moment later a form appeared at the entryway, and a creature, at first they saw what seemed "
                  "like a person, before seeing the rest of its grotesque body, its body looked like a fly's head with "
                  "a human like figure growing out of it, an unspeakable horror")
            print("in the next moment the monster had rushed towards the team, small insect legs carried "
                  "the creature at an incredible speed, it had ripped jonas apart,"
                  "who just a moment ago was stunned and left frozen whilst filming the monstrosity that came "
                  "before them, the monster moved onto the screaming leila and a similar fate befell her.  ")
            print("Leila's scream had awoken Elijah from his stupor and his flight instinct took hold, throwing himself "
                  "over to rappel down the hole, his mind only thought of escape.")
            self.character.choice_survivor(5)
        if ch == '2':
            print("Elijah rappelled down first and when he landed, called out to the team to make their way down"
                  " as well, in the next moment screams from Jonas and Leila were heard overhead, out of Elijah's "
                  "sight he called to them")
            print("when the screamed had ended Elijah prepared to climb back up to find what went wrong, until "
                  "something fell at Elijah's feet, Jonas's body was split from his shoulder through this torso.")
            self.character.choice_survivor(1)

    def middle_story(self):
        pass



    def ending_story(self):
        pass