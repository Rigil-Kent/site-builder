import sections
from abc import ABCMeta, abstractmethod
from configparser import ConfigParser


config = ConfigParser()


class Order(object):
    config = ConfigParser()

    def __init__(self, order="order.cfg"):
        config.read(order)
        self.project = config.get("BasicInfo", "Name")
        self.owner = config.get("BasicInfo", "Owner")
        self.layout = config.get("BasicInfo", "Layout").lower()
        self.bootstrap = config.getboolean("BasicInfo", "Bootstrap")
        self.fontawesome = config.getboolean("BasicInfo", "IconsFA")
        self.colors = [value for key, value in dict(config.items("Colors")).items()]
        self.logo = config.get('Logo', 'File')
        self.pages = [value.lower() for key, value in dict(config.items("Pages")).items()]
        self.slider = [value for key, value in dict(config.items("Slider")).items()]
        self.members = [value for key, value in dict(config.items("Members")).items()]
        self.database = [value for key, value in dict(config.items("Database")).items()]


order = Order()

class Website(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_website()


    @abstractmethod
    def create_website():
        pass


    def get_sections(self):
        return self.sections


    def add_section(self, section):
        self.sections.append(section)

    


class onecolumn(Website):
    def create_website(self):
        self.add_section(sections.BootstrapStart())

        self.add_section(sections.OneCol())
        self.add_section(sections.Footer())

        self.add_section(sections.BootstrapEnd())


class twocolumn(Website):
    def create_website(self):
        self.add_section(sections.BootstrapStart())


        self.add_section(sections.NavbarBasic(order.pages))
        self.add_section(sections.Jumbotron())
        self.add_section(sections.TwoCol())
        self.add_section(sections.Footer())
        
        self.add_section(sections.BootstrapEnd())


class threecolumn(Website):
    def create_website(self):
        self.add_section(sections.BootstrapStart())

        self.add_section(sections.Jumbotron())
        self.add_section(sections.ThreeCol())
        self.add_section(sections.Footer())

        self.add_section(sections.BootstrapEnd())


class bootstrapboilerplate(Website):
    def create_website(self):
        self.add_section(sections.BootstrapStart())
        self.add_section(sections.BootstrapEnd())


class bootstrapfontawesome(Website):
    def create_website(self):
        self.add_section(sections.BootstrapFontAwesome())
        self.add_section(sections.BootstrapEnd())


class simpleblog(Website):
    def create_website(self):
        self.add_section(sections.BootstrapFontAwesome())

        self.add_section(sections.Jumbotron())

        self.add_section(sections.TwoColBlog(col1=3, col2=9, owner=order.owner, nav=order.pages))

        self.add_section(sections.Footer())
        self.add_section(sections.BootstrapEnd())


class band(Website):
    def create_website(self):
        body = "<body id='musicPage' data-spy='scroll' data-target='.navbar' data-offset='50'>"
        self.add_section(sections.BootstrapFontAwesome(body=body))
        self.add_section(sections.BandTemplate(name=order.project, nav=order.pages, members=order.members))
        self.add_section(sections.BootstrapEnd())


class store(Website):
    def create_website(self):
        self.add_section(sections.BootstrapFontAwesome())
        self.add_section(sections.BootstrapEnd())


class administration(Website):
    def create_website(self):
        self.add_section(sections.BootstrapFontAwesome())
        self.add_section(sections.BootstrapEnd())


class portfolio(Website):
    def create_website(self):
        self.add_section(sections.BootstrapFontAwesome())
        self.add_section(sections.BootstrapEnd())


class fromconfig(Website):
    def create_website(self):
        if order.fontawesome:
            self.add_section(sections.BootstrapFontAwesome())
        else:
            self.add_section(sections.BootstrapStart())

        self.add_section(sections.NavbarCentered())
        self.add_section(sections.Jumbotron())
        self.add_section(sections.ThreeCol())
        self.add_section(sections.Footer())
        
        self.add_section(sections.BootstrapEnd())



website_type = order.layout
website = eval(website_type)()
print("Creating another website...", type(website).__name__)
print("Website has sections -- ", website.get_sections())
content = ""
for section in website.sections:
    content += section.content()

with open("index.html", "w") as file:
    file.write(content)
    print("Success")
