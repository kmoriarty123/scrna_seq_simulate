from setuptools import setup, find_packages

setup(
    name='transcript_sampling',
    url='https://gitlab.com/k.moriarty/Life_Science_Course.git',
    author='Kathleen Moriarty',
    author_email='kathleen.moriarty@swisstph.ch',
    description='Transcription Sampler',
    license='MIT',
    version='1.0.0',
    packages=find_packages(),  # this will autodetect Python packages from the directory tree, e.g., in `code/`
    install_requires=[]  # add here packages that are required for your package to run, including version or range of versions
)