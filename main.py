import random

class MysteryDetective:
    def __init__(self):
        self.cases = [
            {"name": "Case of the Missing Necklace", "suspects": ["Alice", "Bob", "Carol"], "culprit": "Bob"},
            {"name": "The Haunted Mansion", "suspects": ["David", "Emily", "Frank"], "culprit": "Emily"},
            {"name": "The Secret Code", "suspects": ["Grace", "Henry", "Isabel"], "culprit": "Henry"}
            # Add more cases as needed
        ]
        self.current_case = random.choice(self.cases)
        self.suspects = self.current_case["suspects"]
        self.culprit = self.current_case["culprit"]
        self.clues = []
        self.inventory = []
    
    def display_intro(self):
        print("Welcome Detective! Let's solve a mystery.")
        print(f"You are investigating: {self.current_case['name']}")
        print("You have gathered at the crime scene with the suspects.")
        print("Interview suspects, collect clues, and deduce the culprit!")
    
    def display_suspects(self):
        print("\nList of suspects:")
        for idx, suspect in enumerate(self.suspects, start=1):
            print(f"{idx}. {suspect}")
    
    def gather_clue(self):
        new_clue = random.choice(["Footprints", "Fingerprint", "Note", "Witness Testimony"])
        self.clues.append(new_clue)
        print(f"You found a clue: {new_clue}")
    
    def interview_suspect(self):
        self.display_suspects()
        suspect_idx = int(input("\nEnter the number of the suspect to interview: ")) - 1
        if 0 <= suspect_idx < len(self.suspects):
            print(f"You are interviewing {self.suspects[suspect_idx]}.")
            if self.suspects[suspect_idx] == self.culprit:
                print(f"{self.suspects[suspect_idx]} confesses! You've caught the culprit.")
                return True
            else:
                print(f"{self.suspects[suspect_idx]} denies involvement.")
        else:
            print("Invalid selection.")
        return False
    
    def deduce_culprit(self):
        print("\nTime to deduce the culprit!")
        print("Reviewing clues and suspect interviews...")
        time.sleep(2)
        
        # Example deduction logic (can be expanded or customized)
        if "Fingerprint" in self.clues:
            print("There was a fingerprint found at the crime scene.")
            if "Note" in self.clues:
                print("The note mentioned a name that matches one of the suspects.")
                if self.clues.count("Footprints") >= 2:
                    print("Multiple sets of footprints were found leading to the suspect.")
                    return True
        print("You lack sufficient evidence to identify the culprit.")
        return False
    
    def play_game(self):
        self.display_intro()
        
        while True:
            action = input("\nEnter your action (gather/interview/deduce/quit): ").strip().lower()
            
            if action == "quit":
                print("Exiting the game. Goodbye, Detective!")
                break
            
            elif action == "gather":
                self.gather_clue()
            
            elif action == "interview":
                if self.interview_suspect():
                    break
            
            elif action == "deduce":
                if self.deduce_culprit():
                    print(f"Congratulations Detective! You solved the case of {self.current_case['name']}.")
                    break
            
            else:
                print("Invalid action! Please choose gather, interview, deduce, or quit.")

if __name__ == "__main__":
    game = MysteryDetective()
    game.play_game()
