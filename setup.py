from setuptools import setup, find_packages

setup(
    name="resale_price_prediction",
    version="0.0.1",
    description="A machine learning project for resale price prediction",
    author="Musa",
    author_email="musaharon07@gmail.com",
    packages=find_packages(exclude=["tests*", "notebooks*", "docs*"]),
    install_requires=[
        # Core dependencies
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.4.0",

        # Optional ML frameworks (add as needed)
        # "tensorflow>=2.5.0",
        # "torch>=1.9.0",
    ],
    python_requires=">=3.8",
)