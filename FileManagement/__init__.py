from os.path import dirname, basename, isfile, join
import glob
FileManagement = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in FileManagement if isfile(f) and not f.endswith('__init__.py')]
