from setuptools import setup, find_packages

setup(
    name="healthsphere-ehr",
    version="1.0.0",
    description="Enterprise Healthcare Information & Clinical EHR Platform",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Clinical Engineering Team",
    author_email="engineering@healthsphere-systems.org",
    packages=find_packages(exclude=["tests*", "generators*"]),
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "healthsphere=main:main",
        ],
    },
)
