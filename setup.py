from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = ""
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name= "ipwebcam",
    packages= ["ipwebcam"],
    version= "0.2.1",
    license= "MIT",
    description= "This is a simple module that helps in accessing the image from the Android App IPWebcam and to be able to display it in pygame",
    author= "Michael Jalloh",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    author_email= "michaeljalloh19@gmail.com",
    url= "https://github.com/Michael-Jalloh/ipwebcam",
    download_url = "https://github.com/Michael-Jalloh/ipwebcam/archive/v_02.1.tar.gz",
    keywords= ["ipwebcam","pygame", "opencv", "cv3","cv2"],
    install_requires=[
        "pygame",
        "opencv-python",
        "numpy",
        "requests"
    ],
    classifiers= [
        "Development Status :: 3 - Alpha",      
        "Intended Audience :: Developers",      
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   
        "Programming Language :: Python :: 3",   
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)