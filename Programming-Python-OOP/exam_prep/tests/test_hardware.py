from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("My name", "Heavy", 500, 500)

    def test_attributes_set(self):
        self.assertEqual(self.hardware.name, "My name")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.capacity, 500)
        self.assertEqual(self.hardware.memory, 500)
        self.assertEqual(self.hardware.software_components, [])

    def test_hardware_has_no_memory_when_software_is_installed_raises(self):
        software = LightSoftware("S name", 501, 501)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_equal_capacity_and_memory_software_is_installed(self):
        software = LightSoftware("S name", 200, 1000)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_software_is_installed(self):
        software = LightSoftware("S name", 20, 20)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_unexisting_software(self):
        software = LightSoftware("S name", 20, 20)
        self.assertEqual(0, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))

        software = LightSoftware("S name", 20, 20)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))

        software_2 = LightSoftware("S2 name", 20, 20)
        self.assertNotIn(software_2, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software_2)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_software(self):
        software = LightSoftware("S name", 20, 20)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        self.assertIn(software, self.hardware.software_components)

        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))
        self.assertNotIn(software, self.hardware.software_components)


if __name__ == '__main__':
    main()