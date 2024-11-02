#!/usr/bin/env
from setuptools import setup

setup(
    name="EasyFirebase",
    version="1.0",
    packages=["EasyFirebase"],
    include_package_data=True,
    license="MIT",
    description="Easy Firebase-django integration.",
    long_description="Djanngo app for easy firebase integration.",
    author="Rubel H.",
    author_email="mail.rubel.me@gmail.com",
    install_requires=[
        "Django>=3.0",
        "firebase-admin==6.5.0",
        "pillow==10.2.0",
    ],
)
