from setuptools import setup, find_packages
from SherlockChain.slither_analyzers import analyser

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="SherlockChain-ai-Scanner",
    description="SherlockChain is a Plutus and Solidity static analysis framework written in Python 3.",
    url="https://github.com/0xQuantumCoder/SherlockChain",
    author="0xQuantumCoder",
    version="0.10.2",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "packaging",
        "prettytable>=3.3.0",
        "pycryptodome>=3.4.6",
        "crytic-compile>=0.3.7,<0.4.0",
        #"crytic-compile@git+https://github.com/crytic/crytic-compile.git@master#egg=crytic-compile",
        "web3>=6.0.0",
        "eth-abi>=4.0.0",
        "eth-typing>=3.0.0",
        "eth-utils>=2.1.0",
    ],
    extras_require={
        "lint": [
            "black==22.3.0",
            "pylint==3.0.3",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "deepdiff",
            "numpy",
            "coverage[toml]",
            "filelock",
            "pytest-insta",
        ],
        "doc": [
            "pdoc",
        ],
        "dev": [
            "slither-analyzer[lint,test,doc]",
            "openai",
        ],
    },
    license="AGPL-3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "SherlockChain = SherlockChain.__main__:main",
            "SherlockChain-check-upgradeability = SherlockChain.tools.upgradeability.__main__:main",
            "SherlockChain-find-paths = SherlockChain.tools.possible_paths.__main__:main",
            "SherlockChain-simil = SherlockChain.tools.similarity.__main__:main",
            "SherlockChain-aiscan = SherlockChain.tools.flattening.__main__:main",
            "SherlockChain-format = SherlockChain.tools.slither_format.__main__:main",
            "SherlockChain-check-erc = SherlockChain.tools.erc_conformance.__main__:main",
            "SherlockChain-check-kspec = SherlockChain.tools.kspec_coverage.__main__:main",
            "SherlockChain-prop = SherlockChain.tools.properties.__main__:main",
            "SherlockChain-mutate = SherlockChain.tools.mutator.__main__:main",
            "SherlockChain-read-storage = SherlockChain.tools.read_storage.__main__:main",
            "SherlockChain-doctor = SherlockChain.tools.doctor.__main__:main",
            "SherlockChain-documentation = SherlockChain.tools.documentation.__main__:main",
            "SherlockChain-interface = SherlockChain.tools.interface.__main__:main",
        ]
    },
)
