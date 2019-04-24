import builder as builder
import sys
import os

commands = {
    "--help": "Returns this help screen",
    "--render": "Renders the selected template"
}

if __name__ == "__main__":
    if len(sys.argv) == 1:
        configuration = builder.order
        new_site = builder.render_template(configuration)
        builder.write_template(new_site)
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".cfg"):
        if os.path.isfile(sys.argv[1]):
            configuration = builder.Order(order=sys.argv[1])
            new_site = builder.render_template(configuration)
            builder.write_template(new_site)
        else:
            print("Couldn't load configuration file. Make sure it exits")
    else:
        command = sys.argv[1]

        if command == "--help" or command == "h":
            for key,value in commands.items():
                print("{} : {}".format(key, value))
        elif command == "--render" or command == "r":
            try:
                print("{}".format(sys.argv[2]))
                template = builder.template_build(sys.argv[2])
                builder.write_template(template)
            except Exception:
                print("Unable to render template.")
        else:
            print("Invalid command")

