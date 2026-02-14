"""
Setup configuration for IAMonJob backend
"""

from setuptools import setup, find_packages

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="iamonjob-backend",
    version="1.0.0",
    author="IAMonJob Team",
    author_email="contact@iamonjob.com",
    description="Backend API for IAMonJob CV analysis application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VOTRE-USERNAME/iamonjobv3",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Flask",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Flask>=3.0.0",
        "flask-cors>=4.0.0",
        "anthropic>=0.39.0",
        "python-dotenv>=1.0.0",
        "Werkzeug>=3.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "safety>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "iamonjob=app:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/VOTRE-USERNAME/iamonjobv3/issues",
        "Source": "https://github.com/VOTRE-USERNAME/iamonjobv3",
        "Documentation": "https://github.com/VOTRE-USERNAME/iamonjobv3/blob/main/README.md",
        "Changelog": "https://github.com/VOTRE-USERNAME/iamonjobv3/blob/main/CHANGELOG.md",
    },
)
