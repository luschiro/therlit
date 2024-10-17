import os

def get_dirs():
    SRC_DIR = os.path.dirname(__file__)
    PROJECT_DIR = os.path.dirname(SRC_DIR)
    DATABASE_DIR = os.path.join(PROJECT_DIR, 'databases')
    THERIAK_DIR = os.path.join(PROJECT_DIR, 'theriak')
    PAGES_DIR = os.path.join(PROJECT_DIR, 'pages')

    dir_dict = {
        'PROJECT' : PROJECT_DIR,
        'SRC' : SRC_DIR,
        'DATABASE' : DATABASE_DIR,
        'THERIAK' : THERIAK_DIR,
        'PAGES' : PAGES_DIR
    }

    return dir_dict

THERIAK_DIR = get_dirs()['THERIAK']