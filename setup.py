from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='waldo',
      version="0.0.1",
      description="TFinding Waldo in a picture",
      license="MIT",
      author="fabianbacher",
      author_email="",
      url="https://github.com/fabianbacher/Wheres-Waldo",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
