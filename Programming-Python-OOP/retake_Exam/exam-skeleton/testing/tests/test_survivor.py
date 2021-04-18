from unittest import TestCase, main

from project.survivor import Survivor


class TestSurvivor(TestCase):
    def test_attributes_set(self):
        subject = Survivor("name", 18)
        self.assertEqual(subject.name, "name")
        self.assertEqual(subject.age, 18)
        self.assertEqual(subject.health, 100)
        self.assertEqual(subject.needs, 100)

    def test_name_not_valid_expect_raises(self):
        with self.assertRaises(ValueError) as ex:
            subject = Survivor("", 18)
        self.assertEqual(str(ex.exception), "Name not valid!")

    def test_age_not_valid_expect_raises(self):
        with self.assertRaises(ValueError) as ex:
            subject = Survivor("name", -10)
        self.assertEqual(str(ex.exception), "Age not valid!")

    def test_health_negative_expect_raises(self):
        subject = Survivor("name", 18)
        with self.assertRaises(ValueError) as ex:
            subject.health = -20
        self.assertEqual(str(ex.exception), "Health not valid!")

    def test_needs_negative_expect_raises(self):
        subject = Survivor("name", 18)
        with self.assertRaises(ValueError) as ex:
            subject.needs = -20
        self.assertEqual(str(ex.exception), "Needs not valid!")

    def test_needs_sustenance_correct(self):
        subject = Survivor("name", 18)
        self.assertEqual(subject.needs_sustenance, False)

    def test_needs_sustenance_false(self):
        subject = Survivor("name", 18)
        subject.needs = 99
        self.assertEqual(subject.needs_sustenance, True)

    def test_needs_haling_correct(self):
        subject = Survivor("name", 18)
        self.assertEqual(subject.needs_healing, False)

    def test_needs_healing_false(self):
        subject = Survivor("name", 18)
        subject.health = 99
        self.assertEqual(subject.needs_healing, True)


if __name__ == '__main__':
    main()