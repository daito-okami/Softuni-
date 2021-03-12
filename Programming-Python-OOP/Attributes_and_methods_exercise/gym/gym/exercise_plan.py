class ExercisePlan:
    _id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan._id += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self._id = ExercisePlan._id

    @staticmethod
    def get_next_id():
        return ExercisePlan._id + 1

    def __repr__(self):
        return f"Plan <{self._id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)
