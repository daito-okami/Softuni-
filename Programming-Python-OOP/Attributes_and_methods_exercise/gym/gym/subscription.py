from Attributes_and_methods_exercise.gym.gym.customer import Customer
from Attributes_and_methods_exercise.gym.gym.equipment import Equipment
from Attributes_and_methods_exercise.gym.gym.exercise_plan import ExercisePlan
from Attributes_and_methods_exercise.gym.gym.gym import Gym
from Attributes_and_methods_exercise.gym.gym.trainer import Trainer


class Subscription:
    _id = 0

    def __init__(self, data, customer_id, trainer_id, exercise_id):
        self.data = data
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        Subscription._id += 1
        self._id = Subscription._id

    def __repr__(self):
        f"Subscription <{self._id}> on {self.data}"

    @staticmethod
    def get_next_id():
        return Subscription._id + 1




customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
