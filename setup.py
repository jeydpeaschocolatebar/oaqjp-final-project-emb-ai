# setup.py

from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='EmotionDetection', # The name of your package
    version='0.1.0',         # The current version of your package
    author='Your Name',      # Your name or organization
    author_email='your.email@example.com', # Your email
    description='A Python package for emotion detection using a Watson NLP service.', # Short description
    long_description=long_description, # Long description from README.md
    long_description_content_type="text/markdown", # Type of long description
    url='https://github.com/yourusername/EmotionDetection', # URL to your project's repository (if applicable)
    packages=find_packages(), # Automatically finds all packages in the current directory
    install_requires=requirements, # List of dependencies from requirements.txt
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Choose your license
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha', # Or 4 - Beta, 5 - Production/Stable
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
    ],
    python_requires='>=3.9', # Minimum Python version required
)