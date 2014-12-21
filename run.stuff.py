import os, sys, subprocess

#-----------------------------------------------------------------------
DO_SCSS = True
SCSS_STYLE = u'compact'   # Opts: nested|expanded|compact|compressed


PELICAN_ROOT = os.path.dirname(os.path.abspath(__file__))
THEME_ROOT = r'C:\_\opt\Python27\Lib\site-packages\pelican\themes'


# -----------------------------------------------------------------------
def main():
    cmd = sys.argv[1].lower() if len(sys.argv) > 0 else 'help'
    if cmd == 'build.dev':
        build_dev()
    elif cmd == 'build.staging':
        build_staging()


#-----------------------------------------------------------------------
def build_dev():
    print '======== Pelican Build - DEV'
    if not DO_SCSS:
        print '-------- NOT processing .scss'
    else:
        print '-------- Processing .scss'
        do_scss(['barenakedcoder.scss', 'pygment.css', 'typogrify.css'], 'barenakedcoder.css')
    subprocess.call([
        'pelican'
        , os.path.join(PELICAN_ROOT, 'content')
        , '-s', os.path.join(PELICAN_ROOT, 'pelicanconf.py')
        , '--delete-output-directory'
        #, '-t', THEME_ROOT + r'\notmyidea'
        #, '-t', THEME_ROOT + r'\simple'
        #, '-t', PELICAN_ROOT + r'\themes-git\aboutwilson'
        , '-t', PELICAN_ROOT + r'\theme-bnc'
        , '-o', os.path.join(PELICAN_ROOT, 'output')
        #, '--debug'
    ])


#-----------------------------------------------------------------------
def build_staging():
    print '======== Pelican Build - DEV'
    if not DO_SCSS:
        print '-------- NOT processing .scss'
    else:
        print '-------- Processing .scss'
        do_scss(['barenakedcoder.scss', 'pygment.css', 'typogrify.css'], 'barenakedcoder.css')
    subprocess.call([
        'pelican'
        , os.path.join(PELICAN_ROOT, 'content')
        , '-s', os.path.join(PELICAN_ROOT, 'pelicanconf_prod.py')
        , '--delete-output-directory'
        #, '-t', THEME_ROOT + r'\notmyidea'
        #, '-t', THEME_ROOT + r'\simple'
        #, '-t', PELICAN_ROOT + r'\themes-git\aboutwilson'
        , '-t', PELICAN_ROOT + r'\theme-bnc'
        , '-o', os.path.join(PELICAN_ROOT, '..', 'Blog-GAE', 'pelican')
        #, '--debug'
    ])


#-----------------------------------------------------------------------
def do_scss(scss_fnames, css_fname):
    scss = ''
    for scss_fn in scss_fnames:
        with open(os.path.join(PELICAN_ROOT, 'theme-bnc', 'static', 'css', scss_fn), 'r') as scss_file:
            scss += scss_file.read()
    from scss.compiler import compile_string
    css = compile_string(scss, output_style=SCSS_STYLE,
        search_path=(os.path.join(PELICAN_ROOT, 'theme-bnc', 'static', 'css')))
    with open(os.path.join(PELICAN_ROOT, 'theme-bnc', 'static', 'css', css_fname), 'w') as css_file:
        css_file.write(css)


main()
