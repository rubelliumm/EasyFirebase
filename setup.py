from setuptools import setup

setup(
    name="EasyFirebase",
    version="2.0",
    packages=["EasyFirebase"],
    include_package_data=True,
    license="MIT",
    description="Easy Firebase-django integration.",
    long_description="Djanngo app for easy firebase integration.",
    author="Md. Rubel H.",
    author_email="mail.rubel.me@gmail.com",
    install_requires=[
        "Django>=3.0",
        "firebase-admin==6.5.0",
        "pillow==10.2.0",
    ],
)
