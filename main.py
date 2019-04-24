import builder as builder
import sys
import os


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        configuration = builder.order
        new_site = builder.render_template(configuration)
        builder.write_template(new_site)
    else:
        if sys.argv[1].endswith(".cfg"):
            if os.path.isfile(sys.argv[1]):
                new_site = builder.render_template(configuration)
                builder.write_template(new_site)
            else:
                print("Couldn't load configuration file. Make sure it exits")
        else:
            print("Not a valid configuration file")

