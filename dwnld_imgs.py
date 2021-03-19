from fastai.vision import *

root_dir = "/content/"
path = Path(root_dir) / 'data'

file='sedan.txt'
dest = path / 'sedan'
dest.mkdir(parents=True, exist_ok=True)

# If you have problems download, try with `max_workers=0` to see exceptions:
download_images(path/file, dest, max_pics=10, max_workers=0)

verify_images(path/c, delete=True, max_size=500)
