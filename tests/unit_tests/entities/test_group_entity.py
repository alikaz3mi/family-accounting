import unittest
from family_accounting.entities import Group


class TestGroupEntity(unittest.TestCase):
    def test_group_creation(self):
        group = Group(group_id=404, name="Family Group", owner_user_id=1, members=[])
        self.assertEqual(group.group_id, 404)
        self.assertEqual(group.name, "Family Group")
        self.assertEqual(group.owner_user_id, 1)
        self.assertEqual(len(group.members), 0)  # Initially no members


if __name__ == "__main__":
    unittest.main()
