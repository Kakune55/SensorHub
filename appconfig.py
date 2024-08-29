import configparser , os, shutil, logging

def conf():
    conf = configparser.ConfigParser()
    if os.path.exists('./conf/app.ini') == False:
        if os.path.exists('./conf/app.example.ini') == False:
            logging.error('file app.ini.example not found')
            exit()
        shutil.copyfile('./conf/app.example.ini', './conf/app.ini')
    conf.read('./conf/app.ini') 
    return conf