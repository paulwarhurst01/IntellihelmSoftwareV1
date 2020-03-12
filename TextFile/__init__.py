from os.path import dirname, basename, isfile, join
import glob
TextFile = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in TextFile if isfile(f) and not f.endswith('__init__.py')]
