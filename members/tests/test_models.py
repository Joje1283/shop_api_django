from django.test import TestCase


from members.models import Member
from ..exceptions import MemberException


class TestMember(TestCase):
    @classmethod
    def setUp(cls):
        member = Member.objects.join(
            username="paul",
            password="1234",
            first_name="jaesik",
            last_name="cho",
            email="paul@test.com",
        )

    def test_회원가입(self):
        # when
        member = Member.objects.first()
        self.assertEqual("paul", member.username)

    def test_중복_회원_제외(self):
        try:
            Member.objects.join(
                username="paul",
                password="1234",
                first_name='"jaesik"',
                last_name='"cho"',
                email="paul@test.com",
            )
        except MemberException as e:
            return
        self.fail()

