from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name = 'CosmoParams',
        description       = "DESC standardized cosmological parameter container",
        author            = "DESC TJP Team",
        version           = "0.1.0",
        license           = "MIT",
        packages          = ['CosmoParams'],
        provides          = ['CosmoParams'],
        include_package_data = True,
        url = "https://github.com/LSSTDESC/CosmoParams",
        )
