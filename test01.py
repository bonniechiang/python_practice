#Bonnie-Practice
import configparser
class Config:
    def _init_(self):
        self.config = configparser.ConfigParser()
        self.config.read('Config.ini')
        
class Print:
    def _init_(self):
        self.config = Config()        
        section_a_Value = self.config.get('Key_DEF')
        section_b_Value = self.config.get('Alarm')

    print ("section_a_Value =  ",section_a_Value )
    print ("section_b_Value =  ",section_b_Value )