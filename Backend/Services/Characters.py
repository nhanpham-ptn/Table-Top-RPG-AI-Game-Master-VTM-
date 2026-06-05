class character():
    def __init__(self, characterSheet:dict):

        self.name = characterSheet["name"]
        self.concept = characterSheet["concept"]
        self.predator = characterSheet["predator"]
        self.sire = characterSheet["sire"]
        self.generation = characterSheet["generation"]
        self.ambition  =  characterSheet["ambition"]
        self.desire  =  characterSheet["desire"]


        self.humanity = 10
        self.health = 10
        self.bloodPotency = 5
        self.masquerade_breach = 10
        
        self.advantage = characterSheet["advantages"]
        self.disadvantage = characterSheet["disadvantages"]

        self.att_count = 22
        self.attributes = attributes(characterSheet["attributes"]["physical"], characterSheet["attributes"]["social"],  characterSheet["attributes"]["mental"])

        self.skill_count = 26
        self.skill = skills(characterSheet["skills"])
        self.clan= clan(characterSheet["clan"], characterSheet["disciplines"])
        self.exp = 0
        self.items = {}        

    def create_attributes(self, attribute: str, sub: str):
        if self.att_count > 0:
            self.attributes.increase(attribute, sub)
            self.att_count -= 1   

    def create_skills(self, category: str, skill: str):
        if self.skill_count > 0:
            self.skill.increase(category, skill)
            self.skill_count -= 1   
        
    def predator_effect(self):
        if self.predator not in PREDATOR_TYPES:
            return
        
        effects = PREDATOR_TYPES[self.predator]

        # --- Attributes ---
        if "attributes" in effects:
            for category, stat, value in effects["attributes"]:
                for _ in range(value):
                    self.attributes.increase(category, stat)

        # --- Skills ---
        if "skills" in effects:
            for category, skill, value in effects["skills"]:
                for _ in range(value):
                    self.skill.increase(category, skill)

        # --- Disciplines ---
        if "disciplines" in effects:
            for discipline in effects["disciplines"]:
                if discipline not in self.disciplines:
                    self.disciplines[discipline] = 0
                self.disciplines[discipline] += 1

    def setting_advan(self, lst): 
        self.advantage = lst

    def setting_disadvan(self, lst): 
        self.advantage = lst

    def access_advantage(self):
        return self.advantage
    
    def access_disadvantage(self):
        return self.disadvantage
    
    def modify_items(self, dict):
        self.items = dict

    def to_dict(self):
        return {
            "name": self.name,
            "concept": self.concept,
            "predator": self.predator,
            "sire": self.sire,
            "generation": self.generation,
            "ambition": self.ambition,
            "desire": self.desire,


            "humanity": self.humanity,
            "blood-potency": self.bloodPotency,
            "health": self.health,
            "masquerade_breach": self.masquerade_breach,



            "clan": self.clan, 


            "attributes": self.attributes.attributes,
            "skills": self.skill.skills,
            "items": self.items,


            "advantages": self.advantage,
            "disadvantages": self.disadvantage,

            "experience": 0
        }

    def getCharacter(self):
        return str(self.to_dict())

        




#---------------------------------------------------------------------------------------------------#

PREDATOR_TYPES = {
            "Alleycat": {
                "rolls": [
                    ("strength", "brawl"),
                    ("wits", "streetwise")
                ],
                "bonuses": {
                    "specialty": [("intimidation", "Stickups"), ("brawl", "Grappling")],
                    "discipline": ["celerity", "potence"],
                    "backgrounds": {"criminal_contacts": 3}
                },
                "penalties": {
                    "humanity": -1
                }
            },

            "Bagger": {
                "rolls": [
                    ("intelligence", "streetwise")
                ],
                "bonuses": {
                    "specialty": [("larceny", "Lockpicking"), ("streetwise", "Black Market")],
                    "discipline": ["obfuscate"],  # conditional in full version
                    "merits": {"iron_gullet": 3}
                },
                "penalties": {
                    "flaws": {"enemy": 2}
                }
            },

            "Blood Leech": {
                "rolls": [],
                "bonuses": {
                    "specialty": [("brawl", "Kindred"), ("stealth", "Against Kindred")],
                    "discipline": ["celerity", "protean"],
                    "blood_potency": 1
                },
                "penalties": {
                    "humanity": -1,
                    "flaws": {
                        "diablerist": 2,
                        "prey_exclusion_mortals": 2
                    }
                }
            },

            "Cleaver": {
                "rolls": [
                    ("manipulation", "subterfuge")
                ],
                "bonuses": {
                    "specialty": [("persuasion", "Gaslighting"), ("subterfuge", "Coverups")],
                    "discipline": ["dominate", "animalism"],
                    "backgrounds": {"herd": 2}
                },
                "penalties": {
                    "flaws": {"dark_secret_cleaver": 1}
                }
            },

            "Consensualist": {
                "rolls": [
                    ("manipulation", "persuasion")
                ],
                "bonuses": {
                    "specialty": [("medicine", "Phlebotomy"), ("persuasion", "Vessels")],
                    "discipline": ["auspex", "fortitude"],
                    "humanity": 1
                },
                "penalties": {
                    "flaws": {
                        "masquerade_breach": 1,
                        "prey_exclusion_nonconsenting": 1
                    }
                }
            },

            "Farmer": {
                "rolls": [
                    ("composure", "animal_ken")
                ],
                "bonuses": {
                    "specialty": [("animal_ken", "Specific Animal"), ("survival", "Hunting")],
                    "discipline": ["animalism", "protean"],
                    "humanity": 1
                },
                "penalties": {
                    "flaws": {"farmer": 2}
                }
            },

            "Osiris": {
                "rolls": [
                    ("manipulation", "subterfuge"),
                    ("intimidation", "performance")
                ],
                "bonuses": {
                    "specialty": [("occult", "Tradition"), ("performance", "Art Form")],
                    "discipline": ["presence"],
                    "backgrounds": {"fame": 3, "herd": 3}
                },
                "penalties": {
                    "flaws": {"enemies": 2}
                }
            },

            "Sandman": {
                "rolls": [
                    ("dexterity", "stealth")
                ],
                "bonuses": {
                    "specialty": [("medicine", "Anesthetics"), ("stealth", "Break-in")],
                    "discipline": ["auspex", "obfuscate"],
                    "backgrounds": {"resources": 1}
                },
                "penalties": {}
            },

            "Scene Queen": {
                "rolls": [
                    ("manipulation", "persuasion")
                ],
                "bonuses": {
                    "specialty": [("etiquette", "Scene"), ("leadership", "Scene"), ("streetwise", "Scene")],
                    "discipline": ["dominate", "potence"],
                    "backgrounds": {"fame": 1, "contacts": 1}
                },
                "penalties": {
                    "flaws": {"disliked_outside_scene": 1}
                }
            },

            "Siren": {
                "rolls": [
                    ("charisma", "subterfuge")
                ],
                "bonuses": {
                    "specialty": [("persuasion", "Seduction"), ("subterfuge", "Seduction")],
                    "discipline": ["presence", "fortitude"],
                    "merits": {"beautiful": 2}
                },
                "penalties": {
                    "flaws": {"enemy": 1}
                }
            },

            "Extortionist": {
                "rolls": [
                    ("strength", "intimidation"),
                    ("manipulation", "intimidation")
                ],
                "bonuses": {
                    "specialty": [("intimidation", "Coercion"), ("larceny", "Security")],
                    "discipline": ["dominate", "potence"],
                    "backgrounds": {"contacts": 3, "resources": 3}
                },
                "penalties": {
                    "flaws": {"enemy": 2}
                }
            },

            "Graverobber": {
                "rolls": [
                    ("resolve", "medicine"),
                    ("manipulation", "insight")
                ],
                "bonuses": {
                    "specialty": [("occult", "Grave Rituals"), ("medicine", "Cadavers")],
                    "discipline": ["fortitude", "oblivion"],
                    "merits": {"iron_gullet": 3},
                    "backgrounds": {"haven": 1}
                },
                "penalties": {
                    "flaws": {"obvious_predator": 2}
                }
            }
        }


class attributes() :
    def __init__(self, physical_stats=None, social_stats=None, mental_stats=None):

        self.attributes = {
            "physical": physical_stats or {
                "strength": 1,
                "dexterity": 1,
                "stamina": 1,
            },

            "social": social_stats or {
                "charisma": 1,
                "manipulation": 1,
                "composure": 1,
            },

            "mental": mental_stats or {
                "intelligence": 1,
                "wits": 1,
                "resolve": 1,
            }
        }

    def access(self, attribute: str, sub: str) :
        return self.attributes[attribute][sub]
    
    def increase(self, attribute: str, sub: str):
        if self.attributes[attribute][sub] <  5:
            self.attributes[attribute][sub] += 1



        

class skills(): 
    def __init__(self, data=None):

        self.skills = data or {
            "physical": {
                "athletics": 0,
                "brawl": 0,
                "craft": 0,
                "drive": 0,
                "firearms": 0,
                "melee": 0,
                "larceny": 0,
                "stealth": 0,
                "survival": 0,
            },

            "social": {
                "animal_ken": 0,
                "etiquette": 0,
                "insight": 0,
                "intimidation": 0,
                "leadership": 0,
                "performance": 0,
                "persuasion": 0,
                "streetwise": 0,
                "subterfuge": 0,
            },

            "mental": {
                "academics": 0,
                "awareness": 0,
                "finance": 0,
                "investigation": 0,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "technology": 0,
            }
        }

    def access(self, category: str, skill: str):
        return self.skills[category][skill]

    def increase(self, category: str, skill: str):
        if self.skills[category][skill] < 5:
            self.skills[category][skill] += 1



class clan():
    def __init__(self, clan: str, preference: dict = None) :
        vampire_clans = {
            "Brujah": {
                "strengths": ["Physical prowess", "Passionate and fierce", "Strong brawlers"],
                "weaknesses": ["Quick temper", "Rebellious", "Prone to frenzy"],
                "disciplines": ["Potence", "Celerity", "Presence"]
            },
            "Gangrel": {
                "strengths": ["Animalistic instincts", "Adapted to survival", "Shapeshifting"],
                "weaknesses": ["Socially isolated", "Animal-like behavior", "Hard to trust"],
                "disciplines": ["Fortitude", "Protean", "Animalism"]
            },
            "Malkavian": {
                "strengths": ["Unique insight", "Unpredictable creativity", "Clairvoyant tendencies"],
                "weaknesses": ["Madness", "Erratic behavior", "Hard to read"],
                "disciplines": ["Auspex", "Dementation", "Obfuscate"]
            },
            "Nosferatu": {
                "strengths": ["Information gathering", "Stealth and infiltration", "Resilient"],
                "weaknesses": ["Horrific appearance", "Social stigma", "Trust issues"],
                "disciplines": ["Obfuscate", "Potence", "Animalism"]
            },
            "Toreador": {
                "strengths": ["Charismatic", "Artistic influence", "Socially adept"],
                "weaknesses": ["Obsessive with beauty", "Easily distracted", "Vanity"],
                "disciplines": ["Auspex", "Celerity", "Presence"]
            },
            "Tremere": {
                "strengths": ["Magical knowledge", "Strategic and organized", "Clan solidarity"],
                "weaknesses": ["Rigid hierarchy", "Dependence on blood magic", "Paranoid"],
                "disciplines": ["Thaumaturgy", "Dominate", "Auspex"]
            },
            "Ventrue": {
                "strengths": ["Leadership", "Social influence", "Wealth and power"],
                "weaknesses": ["Picky about feeding", "Arrogant", "Rigid traditions"],
                "disciplines": ["Dominate", "Fortitude", "Presence"]
            },
            "Caitiff": {
                "strengths": ["Adaptive", "Versatile", "Not bound by clan restrictions"],
                "weaknesses": ["No clan powers", "Socially marginalized", "High danger from elders"],
                "disciplines": ["Varies individually", "No inherent clan disciplines"]
            } ,
            "Thin-blood": {
                "strengths": ["Versatile", "Not bound by clan restrictions", "Able to tolerate sunlight", "Lifelike"],
                "weaknesses": ["No clan powers", "Socially marginalized", "High danger from elders"],
                "disciplines": ["Thin-blood Alchemy"]
            }
        }
        self.clan = vampire_clans[clan]

        if (preference != None):
            disciplines = preference
        else:
            disciplines = vampire_clans[clan]["disciplines"]
        
        base_disciplines = {
            d: 1 for d in disciplines
        }

        self.clan["disciplines"] = base_disciplines
    
    def access(self): 
        return self.clan
    
    def increase(self, discipline):
        if self.clan["disciplines"][discipline] < 5:
            self.clan["disciplines"][discipline] += 1
