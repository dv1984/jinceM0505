# coding:UTF-8
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "www.jince-tech.com-%s" % os.urandom(24)
    MAX_CONTENT_LENGTH = 8 * 1024 *1024
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR,'statci/upload')
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://jince_db_01:Jince0331@rm-bp1561n11704142t89o.mysql.rds.aliyuncs.com:3306/jince"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
config ={
    "development":DevelopmentConfig,
}