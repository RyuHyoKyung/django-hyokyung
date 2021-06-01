from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()  # 인스턴스 생성
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train.test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this  # 데이터프레임


    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train 의 type 은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.test.columns} 이다.')
        print(f'Test 의 type 은 {type(this.train)} 이다.')
        print(f'Test 의 column 은 {this.test.columns} 이다.')
        return this