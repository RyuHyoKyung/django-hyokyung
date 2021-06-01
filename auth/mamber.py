#회원가입,아이디,본명,이메일,로그인,마이페이지,내정보수정,회원탈퇴
class Member(object):

    id = ''
    pw = ''
    name = ''
    email = ''

    def login(self):
        pass

    def mypage(self):
        pass

    def join(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    @staticmethod
    def main():
       member = Member()
       while 1:
            menu = int(input('0.나가기\n1.회원가입\n2.로그인\n3.마이페이지\n4.회원정보수정\n5.회원탈퇴'))

            if menu == 0:
                break

            elif menu == 1:
                member.id = ''
                member.pw = ''
                member.name = ''
                member.email = ''
                member.join()

            elif menu == 2:
                member.id = ''
                member.pw = ''
                member.login()

            elif menu == 3:
                member.id = ''
                member.mypage()

            elif menu == 4:
                member.id = ''
                member.pw = ''
                member.name = ''
                member.email = ''
                member.update()

            elif menu == 5:
                member.id = ''
                member.pw = ''
                member.remove()

            else:
                print('없는 번호')
                continue
Member.main()





