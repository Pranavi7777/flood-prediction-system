"""
Setup script for Flood Prediction System
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flood-prediction-system",
    version="1.0.0",
    author="Sai Pranavi Karumuri",
    author_email="176794559+Pranavi7777@users.noreply.github.com",
    description="AI-powered flood risk prediction using machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pranavi7777/flood-prediction-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.3.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "xgboost>=2.0.0",
        "joblib>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "openpyxl>=3.1.0",
    ],
    entry_points={
        "console_scripts": [
            "flood-predict=flask.app:main",
        ],
    },
    keywords="machine-learning flood-prediction xgboost flask data-science",
    project_urls={
        "Bug Reports": "https://github.com/Pranavi7777/flood-prediction-system/issues",
        "Source": "https://github.com/Pranavi7777/flood-prediction-system",
    },
)
