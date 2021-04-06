from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Test1")

    def test_attributes_are_set(self):
        self.assertEqual("Test1", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)

    def test_enroll_course_with_notes(self):
        result = self.student_1.enroll("Python_OOP", ['Inheritance', 'SOLID'])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python_OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_courses_with_notes_without_saving_them(self):
        result = self.student_1.enroll("Python_OOP", ['Inheritance', 'SOLID'], 'N')
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(0, len(self.student_1.courses["Python_OOP"]))
        self.assertEqual("Course has been added.", result)

    def test_enroll_add_notes_to_existing_course(self):
        # setup
        result = self.student_1.enroll("Python_OOP", ['Inheritance', 'SOLID'])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python_OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        # test if new notes are appended to existing course
        result = self.student_1.enroll("Python_OOP", ['Abstraction', 'Testing'])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(4, len(self.student_1.courses["Python_OOP"]))
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_to_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("Python OOP", ["1", 2])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_existing_course(self):
        # setup
        result = self.student_1.enroll("Python_OOP", ['Inheritance', 'SOLID'])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python_OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        result = self.student_1.add_notes("Python_OOP", "testing")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(3, len(self.student_1.courses["Python_OOP"]))
        self.assertIn("testing", self.student_1.courses["Python_OOP"])

    def test_add_unexisting_course_removal_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Python OOp")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_1.enroll("Python_OOP", ['Inheritance', 'SOLID'])
        self.assertEqual(1, len(self.student_1.courses))

        result = self.student_1.leave_course("Python_OOP")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(0, len(self.student_1.courses))


if __name__ == '__main__':
    main()
