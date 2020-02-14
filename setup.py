import setuptools

setuptools.setup(
    name="life-cycle-hooks",
    version="0.0.1",
    author="Sebastian Werner",
    author_email="werner@tu-berlin.de",
    description="A small life-cycle-hooks api for smile-openwhisk",
    url="https://github.com/ISE-SMILE/runtime-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)