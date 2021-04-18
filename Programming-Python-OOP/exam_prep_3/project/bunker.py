class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        self.food = []
        self.water = []
        self.painkillers = []
        self.salves = []


    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists,")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            for m in self.medicine:
                if m == medicine_type:
                    find_index = self.medicine.index(m)
                    found_med = self.medicine.pop(find_index)
                    found_med.apply(survivor)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            for m in self.supplies:
                if m == sustenance_type:
                    find_index = self.supplies.index(m)
                    found_sustenance = self.supplies.pop(find_index)
                    found_sustenance.apply(survivor)
                    return f"{survivor.name} healed successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age_multiplyer
            # TODO give water and food