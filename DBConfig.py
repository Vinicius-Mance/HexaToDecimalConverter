import configparser

def DBConfig(filepath):

    db = {}
    config = configparser.ConfigParser()
    config.read(filepath)

    db['host'] = config['mysql']['host']
    db['user'] = config['mysql']['user']
    db['password'] = config['mysql']['password']
    db['database'] = config['mysql']['database']

    return db
