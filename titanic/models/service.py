from titanic.models.dataset import Dataset
import pandas as pd

class Service(object):

    dataset = Dataset()     # 인스턴스만들기

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1)  # 0은 가로 1은 세로


    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:  # drop_feature 필요없는 데이터 컬럼 지우기
        this.train = this.train.drop(['feature'], axis = 1)
        return this

