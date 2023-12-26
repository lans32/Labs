from operator import itemgetter
import unittest

class Computer:
    def __init__(self, computer_id, brand, model, os_id):
        self.computer_id = computer_id
        self.brand = brand
        self.model = model
        self.os_id = os_id

class OperatingSystem:
    def __init__(self, os_id, name):
        self.os_id = os_id
        self.name = name

class ComputerOS:
    def __init__(self, computer_id, os_id):
        self.computer_id = computer_id
        self.os_id = os_id

class ComputerManager:
    def __init__(self, computers, operating_systems, computer_os_relationship):
        self.computers = computers
        self.operating_systems = operating_systems
        self.computer_os_relationship = computer_os_relationship

    def get_computers_with_os(self):
        return [(c.brand, c.model, os.name)
                for c in self.computers
                for os in self.operating_systems
                if c.os_id == os.os_id]

    def get_os_computer_count(self):
        os_counts = {}
        for os in self.operating_systems:
            os_name = os.name
            os_computers = list(filter(lambda i: i[2] == os_name, self.get_computers_with_os()))
            os_counts[os_name] = len(os_computers)
        return os_counts

    def get_windows_computers(self):
        return [(c.brand, c.model, os_name)
                for os_name, computer_id, os_id in self.get_os_computer_relationship()
                if 'Windows' in os_name
                for c in self.computers if c.computer_id == computer_id]

    def get_os_computer_relationship(self):
        return [(os.name, co.computer_id, co.os_id)
                for os in self.operating_systems
                for co in self.computer_os_relationship
                if os.os_id == co.os_id]

class TestComputerManager(unittest.TestCase):
    def setUp(self):
        computers = [
            Computer(1, 'Dell', 'XPS 13', 1),
            Computer(2, 'HP', 'EliteBook', 2),
            Computer(3, 'Apple', 'MacBook Pro', 3),
            Computer(4, 'Lenovo', 'ThinkPad', 1),
            Computer(5, 'Asus', 'ZenBook', 2),
        ]

        operating_systems = [
            OperatingSystem(1, 'Windows 10'),
            OperatingSystem(2, 'Ubuntu 20.04'),
            OperatingSystem(3, 'macOS'),
        ]

        computer_os_relationship = [
            ComputerOS(1, 1),
            ComputerOS(2, 2),
            ComputerOS(3, 3),
            ComputerOS(4, 1),
            ComputerOS(5, 2),
        ]

        self.computer_manager = ComputerManager(computers, operating_systems, computer_os_relationship)

    def test_get_computers_with_os(self):
        result = self.computer_manager.get_computers_with_os()
        self.assertEqual(len(result), 5)

    def test_get_os_computer_count(self):
        result = self.computer_manager.get_os_computer_count()
        self.assertEqual(result['Windows 10'], 2)
        self.assertEqual(result['Ubuntu 20.04'], 2)
        self.assertEqual(result['macOS'], 1)

    def test_get_windows_computers(self):
        result = self.computer_manager.get_windows_computers()
        self.assertEqual(len(result), 2)
        self.assertIn(('Dell', 'XPS 13', 'Windows 10'), result)
        self.assertIn(('Lenovo', 'ThinkPad', 'Windows 10'), result)

if __name__ == '__main__':
    unittest.main()
