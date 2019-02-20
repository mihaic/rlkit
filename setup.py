from setuptools import find_packages, setup

setup(
    name="rlkit-python",  # Not real name, just placeholder
    packages=find_packages(),
    install_requires=[  # Not exhaustive
        "gtimer",
        "joblib",
        "torch",
    ],
)
