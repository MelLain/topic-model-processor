# Topic Model Processor (2019)

from setuptools import setup, find_packages

setup_kwargs = dict(
    name='topic_model_processor',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    setup_requires=[
        'numpy'
    ],
)

setup(**setup_kwargs)

