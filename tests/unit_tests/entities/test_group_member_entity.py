import unittest
from family_accounting.entities import GroupMember
from family_accounting.entities.group_member import AccessLevel


class TestGroupMemberEntity(unittest.TestCase):
    def test_group_member_creation(self):
        group_member = GroupMember(
            group_member_id=303,
            group_id=1,
            user_id=1,
            access_level=AccessLevel.OWNER,
        )
        self.assertEqual(group_member.group_member_id, 303)
        self.assertEqual(group_member.group_id, 1)
        self.assertEqual(group_member.user_id, 1)
        self.assertEqual(group_member.access_level, AccessLevel.OWNER)


if __name__ == "__main__":
    unittest.main()
