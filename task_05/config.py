from configparser import ConfigParser 


def config(filename='database.ini', section='postgresql'):
    """This function loads the PostgreSQL database connectivity configuration from the external file.

    Kwargs:
        filename (str): file name having config params 
        section (str): section name (database name)

    Returns: (dict) a dictionary of db connection params

    """
    # create a parser
    parser = ConfigParser()
    # read the config file
    parser.read(filename)

    # get section, default to postgresql 
    db={}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    else:
        raise Exception('Section {0} not found in the {1}file'.format(section, filename))

    return db

if __name__ == "__main__":
    db_params = config()
    print(db_params)
