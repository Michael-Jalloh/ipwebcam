from distutils.core import setup
setup(
    name= "ipwebcam",
    packages= ["ipwebcam"],
    version= "0.1",
    license= "MIT",
    description= "This is a simple module that helps in accessing the image from the Android App IPWebcam and to be able to display it in pygame",
    author= "Michael Jalloh",
    author_email= "michaeljalloh19@gmail.com",
    url= "https://github.com/Michael-Jalloh/ipwebcam",
    download_url = "https://github.com/Michael-Jalloh/ipwebcam/archive/v_01.tar.gz",
    keywords= ["ipwebcam","pygame", "opencv", "cv3","cv2"],
    install_requires=[
        "pygame",
        "opencv-python",
        "numpy",
        "requests"
    ],
    classifiers= [
        "Development Status :: 3 - Alpha",      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",      # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   # Again, pick a license
        "Programming Language :: Python :: 3",      #Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)