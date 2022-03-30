import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smms-cascades",
    version="1.0.3",
    author="cascades",
    author_email="cascades@sjtu.edu.cn",
    description="A command line HTTP client to of https://sm.ms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cascades-sjtu/smms-cli",
    project_urls={
        "Bug Tracker": "https://github.com/cascades-sjtu/smms-cli/issues",
    },
    # command line
    entry_points={"console_scripts": ["smms = smms.smms:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
