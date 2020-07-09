from setuptools import setup, find_packages

setup(
    name='gwf-graph',
    version='0.0.1',
    author="Per Høgfeldt",

    packages=find_packages("src"),
    package_dir={"": "src"},

    entry_points={
        'gwf.plugins': ['graph = gwf_graph.main:graph']
    },

    python_requires=">=3.6",
    install_requires=[
        'gwf>=1.7.2',
    ],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
