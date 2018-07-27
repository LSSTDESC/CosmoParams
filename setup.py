from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name = 'CosmoParams',
        description       = "DESC standardized cosmological parameter container",
        author            = "DESC TJP Team",
        packages = find_packages(),
        include_package_data = True,
        )
