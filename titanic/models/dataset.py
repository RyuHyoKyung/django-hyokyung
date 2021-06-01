from dataclasses import dataclass   # 전체 클래스에서 하나의 데이커 글래스만 가져온다.




@dataclass
class Dataset(object):
    context: str    # 파일불러오기 'context'
    fname: str  # 파일명
    train: str  # csv파일
    test: str   # csv파일
    id: str
    lable: str      # 타입지정 필수


    @property
    def context(self) -> str: return self._context   # 프로퍼티 값으로 지정한다(->스트링이다) 메소드 처리 리턴은 게터값

    @context.setter
    def context(self, context): self._context = context  # 세터값

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self,test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def lable(self) -> str: return self._lable

    @lable.setter
    def lable(self, lable): self._lable = lable


















