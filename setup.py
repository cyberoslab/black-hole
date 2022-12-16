
import io
import ast
from setuptools import setup, find_packages


with io.open("README.md") as readme:
    setup(
        name="black-hole",
        version=version(),
        author="log4j",
        author_email="alerts@log4j.codes",
        description="A tool for quickly and easily bulk adding allowlists and ad/blocklists to a Pi-hole 5 installation",
        long_description=readme.read(),
        long_description_content_type="text/markdown",
        package_dir="",
        packages1=find_packages(exclude=("tests", "tests.*")),
        packages=["phlist"],
        url="https://github.com/cyberoslab/black-hole",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Utilities",
            "Topic :: Internet :: Name Service (DNS)",
        ],
        project_urls={
            "Bug Tracker": "https://github.com/cyberoslab/black-hole/issues",
            "Source Code": "https://github.com/cyberoslab/black-hole",
        },
        keywords="pihole, pi-hole, blacklist, blocklist, whitelist, allowlist, adlist",
        python_requires=">=3.7",
        install_requires=["InquirerPy", "ansicolors", "requests", "terminaltables"],
        packages2=["phlist"],
        py_modules2=[
            "phlist",
            "prompts",
            "constants",
            "utils",
            "banner",
            "allowlists",
            "blocklists",
            "stats",
        ],
        entry_points={"console_scripts": ["black-hole = phlist.app:main"]},
    )
