import os, sys, subprocess

PELICAN_ROOT = os.path.dirname(os.path.abspath(__file__))
THEME_ROOT = r'C:\_\opt\Python27\Lib\site-packages\pelican\themes'


# -----------------------------------------------------------------------
def main():
    cmd = sys.argv[1].lower() if len(sys.argv) > 0 else 'help'
    if cmd == 'build.dev':
        build_dev()


#-----------------------------------------------------------------------
def build_dev():
    print '======== Pelican Build - DEV'
    subprocess.call([
        'pelican'
        , os.path.join(PELICAN_ROOT, 'content')
        , '-s', os.path.join(PELICAN_ROOT, 'pelicanconf.py')
        , '--delete-output-directory'
        #, '-t', THEME_ROOT + r'\notmyidea'
        #, '-t', THEME_ROOT + r'\simple'
        , '-t', PELICAN_ROOT + r'\theme-bnc'
        , '-o', os.path.join(PELICAN_ROOT, 'output')
    ])


#-----------------------------------------------------------------------
def build_staging():
    pass


main()
