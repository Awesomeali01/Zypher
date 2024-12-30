from setuptools import setup

# Read the contents of the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="zypher",  
    version="1.0.0", 
    description="A Flet-based framework for rapid application development with Supabase integration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ali Khan - The Space Dev",
    author_email="ali.bgmi.in@gmail.com",
    url="https://github.com/Awesomeali01/Zypher",  
    py_modules=["zypher"],  
    install_requires=[
        "flet==0.23.0",  
        "supabase>=1.0.0",  
        "python-dotenv>=1.0.0",
        "typer>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "zypher=zypher.zypher:cli",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    keywords="flet, supabase, app framework, CLI",
    project_urls={
        "Bug Tracker": "https://github.com/Awesomeali01/Zypher/issues",
        "Documentation": "https://github.com/Awesomeali01/Zypher/wiki",
        "Source Code": "https://github.com/Awesomeali01/Zypher",
    },
)
