from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def description(self):
        pass


#region Bootstrap 4
class BootstrapEntry(Section):
    def __init__(self, style=None, js=None, body=None):
        self.body = body
        self.style = style
        self.js = js


    def __repr__(self):
        return "Bootstrap | CSS"

    def get_resources(self):
        resources = "<!-- Template Resources -->"
        if self.style is not None:
            resources += self.style
            
        if self.js is not None:
            resources += self.js

        return resources

    def content(self):

        content = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    {}

    <style>
        .row.content {height: 1500px;}
        .sidenav {
      background-color: #f1f1f1;
      height: 100%;
    }

    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height: auto;} 
    }
    </style>

    <title>Hello, world!</title>
  </head>'''.format(self.get_resources())

        if self.body is not None:
            body = self.body
        else:
            body = '''
  <body>
  '''
        return content + body


    def description(self):
        return "Bootstrap | CSS"

class BootstrapEntryFontAwesome(Section):

    def __init__(self, style=None, js=None, body=None):
        self.body = body
        self.js= js
        self.style = style

    def __repr__(self):
        return "Bootstrap | CSS | Font Awesome"

    def get_resources(self):
        resources = "<!-- Template Resources -->"
        if self.style is not None:
            resources += self.style
            
        if self.js is not None:
            resources += self.js

        return resources

    def content(self):
        content = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    
    <!-- Font Awesome CSS -->
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">

    
    {}

    <title>Hello, world!</title>
  </head>'''.format(self.get_resources())
    
        if self.body is not None:
            body = self.body
        else:
            body = '''
  <body>
  '''
        return content + body


    def description(self):
        return "Bootstrap | CSS"

#endregion Bootstrap 4

#region NavBar

#region Unbranded
class NavbarBasic(Section):
    def __init__(self, data):
        self.data = data

    def __repr(self):
        return "Navbar"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        start = '''
<nav class="navbar navbar-expand-sm bg-light">
    <ul class="navbar-nav">
    '''

        links =  self.get_data(self.data)
        
        end = '''
    </ul>
</nav>
'''

        content = start + links + end
        return content


    
    def description(self):
        return "Basic bootstrap NavBar - grey horizontal navbar that becomes vertical on small screens"


class NavbarBasicVert(Section):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Navbar | Vertical"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items
        
    def content(self):
        start = '''
    <nav class="navbar bg-light">
        <ul class="navbar-nav">
        '''

        links = get_data(self.data)

        end = '''
    </ul>
</nav>
        '''

        content = start + links + end

        return content
        


    def description(self):
        return "Basic bootstrap vertical navbar - light"


class NavbarCentered(Section):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Navbar | Centered"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        start = '''
<nav class="navbar navbar-expand-sm bg-light justify-content-center">
    <ul class="navbar-nav">
        '''

        links = get_data(self.data)

        end = '''
    </ul>
</nav>
        '''

        content = start + links + end
        return content
        

    def description(self):
        return "Basic Bootstrap navbar - centered"

#endregion Branded


#region Branded Text
class NavbarBrandedText(Section):
    def __init__(self, logo, data):
        self.data = data
        self.logo = logo

    def __repr__(self):
        return "Navbar | Branded | Text only"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        start = '''
        <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
            <a class="navbar-brnd" href="#">{}</a>
            <ul class="navbar-nav">
        '''.format(self.logo)

        links = get_data(self.data)

        end = '''
    </ul>
</nav>
        '''

        content = start + links + end
        return content

    def description(self):
        return "Bootstrap branded navbar - text only"


class NavbarTopFixedBrandedText(Section):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Navbar | Branded | Fixed Top | Text Only"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        start = '''
<nav class="navbar navbar-expand-sm bg-dark navbar navbar-dark fixed-top">
    <a class="navbar-brnd" href="#">
        <img src="" alt="Logo" style="width:40px;">
    </a>
    <ul class="navbar-nav">
        '''

        links = get_data(self.data)

        end = '''
    </ul>
</nav>
        '''

        content = start + links + end

        return content


    def description(self):
        return "Bootstrap 4 top fixed branded navbar - image logo"

#endregion Branded Text

#region Branded Image
class NavbarBrandedImg(Section):
    def __init__(self, logo, data):
        self.logo = logo
        self.data = data

    def __repr__(self):
        return "Navbar | Branded | Image"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        start = '''
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <a class="navbar-brnd" href="#">
        <img src="{}" alt="Logo" style="width:40px;">
    </a>
    <ul class="navbar-nav">
        '''.format(self.logo)

        links = get_data(self.data)

        end = '''
    </ul>
</nav>
        '''

        content = start + links + end

        return content

    def description(self):
        return "Boostrap 4 branded navbar - image logos"


class NavbarTopFixedBrandedImg(Section):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Navbar | Branded | Fixed Top | Text Only"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        start = '''
<nav class="navbar navbar-expand-sm bg-dark navbar navbar-dark fixed-top">
    <a class="navbar-brnd" href="#">
        <img src="" alt="Logo" style="width:40px;">
    </a>
    <ul class="navbar-nav">
        '''

        links = get_data(self.data)

        end = '''
    </ul>
</nav>
        '''

        content = start + links + end

        return content


    def description(self):
        return "Bootstrap 4 top fixed branded navbar - image logo"

#endregion NavBar


#region Jumbotron
class Jumbotron(Section):
    def __repr__(self):
        return "Jumbotron"

    def content(self):
        return '''
<div class="jumbotron">
    <h1>Jumbotron</h1>
    <p>Text content</p>
</div>
        '''

    def description(self):
        return "Bootstrap 4 jumbotron"


class JumbotronFullWidth(Section):
    def __repr__(self):
        return "Full Width Jumbotron"

    def content(self):
        return '''
<div class="jumbotron jumbotron-fluid">
    <div class="container">
        <h1>Jumbotron</h1>
        <p>Text content</p>
    </div>
<div>
        '''
    
    def description(self):
        return "Bootstrap 4 jumbotron - full width"
#endregion Jumbotron


#region Basic Col Layout(s)
class OneCol(Section):
    def __repr__(self):
        return "One Col layout"

    def content(self):
        return '''
<div class="container">
    <div class="row"
        <div class="col">
            <p>Single Column</p>
        </div>
    </div>
</div>
        '''

    def description(self):
        return "Container containing a single row and column"


#region Two Col Layouts
class TwoCol(Section):
    def __init__(self, col1=None, col2=None):
        self.col1 = col1
        self.col2 = col2

    def __repr__(self):
        return "Two Col layout"

    def content(self):
        if self.col2 is not None:
            return '''
<div class="container-fluid">
    <div class="row">
        <div class="col-sm-{}">
            <p>Two column</p>
        </div>

        <div class="col-sm-{}">
            <p>Two Column</p>
        </div>
    </div>
</div>
        '''.format(self.col1, self.col2)
        else:
            return '''
<div class="container-fluid">
    <div class="row">
        <div class="col-sm">
            <p>Two column</p>
        </div>

        <div class="col-sm">
            <p>Two Column</p>
        </div>
    </div>
</div>
        '''


    def description(self):
        return "Container containing single row and two columns"

#region Two Col Blog
class TwoColBlog(Section):
    def __init__(self, col1=None, col2=None, owner=None, nav=None):
        self.col1 = col1
        self.col2 = col2
        self.nav = nav
        self.owner = owner

    def __repr__(self):
        return "Two Col Blog layout"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link nav-pills" href="#">{}</a>
        </li>
        '''.format(link)

        return nav_items

    def content(self):
        if self.col2 is not None:
            return '''
<div class="container-fluid">
    <div class="row content">
        <div class="col-sm-{} sidenav">
            <h4>{}'s Blog<h4>
            <ul class="nav flex-column">'''.format(self.col1, self.owner) + self.get_data(self.nav) + '''

                <li>
                    <form class="form-inline" action="">
                        <input class="form-control mr-sm-2" type="text" placeholder="search">
                        <button class="btn btn-success" type="submit">search</button>
                    </form>
                </li>
            </ul>
        </div>

        <div class="col-sm-{}">
            <h3><small>Recent Posts</small></h4>
            <hr>
            <h2>Introducing: Automated Blog Site!</h2>
            <h5><span class="fa fa-clock-o"></span> Posted by Admin, April 20, 2019</h5>
            <h5><span class="badge badge-success">Lorem</span></h5><br>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            
            <hr>

            <h4>Leave a Comment:</h4>
            <form role="form">
                <div class="form-group">
                    <textarea class="form-control" rows="3" required></textarea>
                </div>
                <button type="submit" class="btn btn-success">Submit</button>
            </form>
            <br><br>

            <p><span class="badge badge-secondary">2</span> Comments:</p><br>

            <div class="row">

                <div class="col-sm-2 text-center">
                    <img src="bird.jpg" class="rounded-circle" height="65" width="65" alt="Avatar">
                </div>

                <div class="col-sm-10">
                    <h4>SomeDude <small>April 20, 2019, 3:00 PM</small></h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <br>
                </div>

                <div class="col-sm-2 text-center">
                    <img src="bandmember.jpg" class="rounded-circle" height="65" width="65" alt="Avatar">
                </div>

                <div class="col-sm-10">
                    <h4>SomeGuy <small>April 20, 2019, 4:00 PM</small></h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <br>
                    <p><span class="badge badge-secondary">1</span> Comment:</p><br>

                    <div class="row">
                        <div class="col-sm-2 text-center">
                            <img src="bird.jpg" class="rounded-circle" height="65" width="65" alt="Avatar">
                        </div>
                        <div class="col-sm-8">
                            <h4>NestedDude <small>April 21, 2019, 8:20 AM</small></h4>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                            <br>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

</div>
        '''.format(self.col2)
        else:
            return '''
<div class="container-fluid">
    <div class="row">
        <div class="col-sm">
            <p>Two column</p>
        </div>

        <div class="col-sm">
            <p>Two Column</p>
        </div>
    </div>
</div>'''

    def description(self):
        return "Simple Two Column Blog Layout"
#endregion Two Col Blog


#endregion Two Col Layouts

class ThreeCol(Section):
    def __repr__(self):
        return "Three Col layout"

    def content(self):
        return '''
<div class="container">
    <div class="row">
        <div class="col-sm">
            <p>Three Col</p>
        </div>

        <div class="col-sm">
            <p>Three Col</p>
        </div>

        <div class="col-sm">
            <p>Three Col</p>
        </div>
    </div>
</div>
        '''

    def description(self):
        return "Container containing single row and three columns"


#endregion Basic Col Layout(s)


#region Templates

#region Band Template
class BandTemplate(Section):

    def __init__(self, name=None, nav=None, members=None):
        self.name = name
        self.nav = nav
        self.members = members

    def __repr__(self):
        return "Bootstrap 4 Band Template"

    def __repr(self):
        return "Navbar"

    def get_data(self, data):
        nav_items = ""
        for link in data:
            nav_items += '''
        <li class="nav-item">
            <a class="nav-link" href="#{}">{}</a>
        </li>
        '''.format(link, link)

        return nav_items
    
    def get_member_info(self, data):
        data.split(',')
        name = data[0]
        instrument = data[1]
        fact = data[2]
        joindate = data[3]

        return name, instrument, fact, joindate

    def content(self):
        navigation = '''
<nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggler collapsed" data-toggle="collapse" data-target="#navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <a class="navbar-brand" href="#musicPage">{}</a>
        </div>


        <div class="collapse navbar-collapse" id="navigation">
            <ul class="nav navbar-nav ml-auto">
            {}
            </ul>
        </div>
    </div>

    
</nav>
        '''.format(self.name, self.get_data(self.nav))

        slider = '''
<div id="slider" class="carousel slide container-fluid" data-ride="carousel" style="padding:0 0; margin: 0, 0; overflow: hidden;">

    <div class="row">

        <div class="col">
            <ul class="carousel-indicators">
                <li data-target="#slider" data-slide-to="0" class="active"></li>
                <li data-target="#slider" data-slide-to="1"></li>
                <li data-target="#slider" data-slide-to="2"></li>
            </ul>

            <div class="carousel-inner">

                <div class="carousel-item active">
                    <img src="ny.jpg" alt="NY" class="img-fluid w-100">
                    <div class="carousel-caption">
                        <h3>New York</h3>
                        <p>Atmosphere finally made a good album.</p>
                    </div>
                </div>

                <div class="carousel-item">
                    <img src="chicago.jpg" alt="Chigao" class="img-fluid w-100">
                    <div class="carousel-caption">
                        <h3>Chicago</h3>
                        <p>Chillin' out Chi-Town</p>
                    </div>
                </div>

                <div class="carousel-item">
                    <img src="la.jpg" alt="Los Angeles" class="img-fluid w-100">
                    <div class="carousel-caption">
                        <h3>L.A.</h3>
                        <p>Traffic was unholy to say the least...</p>
                    </div>
                </div>

            </div>



            <a class="carousel-control-prev" href="#slider" data-slide="prev">
                <span class="carousel-control-prev-icon"></span>
            </a>
            <a class="carousel-control-next" href="#slider" data-slide="next">
                <span class="carousel-control-next-icon"></span>
            </a>
        </div>
    </div>
</div>
        '''


        about = '''
<div id="about" class="container text-center">
    <div class="row">
        <div class="col">
            <h3>{}</h3>
            <p><em>We LIVE for the music</em></p>
            <p>We have created a fictional band website. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
    </div>
    

        '''.format(self.name)


        roster = "<div class=\"row\">"
        index = 1
        for member in self.members:
            data = member.split(',')
            roster += '''

    <div class="col-sm-4">
        <p class="text-center"><strong>{}</strong></p>
        <a href="" data-toggle="collapse" data-target="#bandmember{}">
            <img src="bandmember.jpg" class="rounded-circle person" alt="" width="255" height="255">
        </a>
        <div id="bandmember{}" class="collapse">
            <p>{}</p>
            <p>{}</p>
            <p>Member since {}</p>
        </div>
    </div>

            '''.format(data[0], index, index, data[1], data[2], data[3])
            index += 1

        roster += "</div>"

        tour = '''
        <div id="tour" class="container-fluid bg-1">
            <div class="">
                <h3 class="text-center">Tour Dates</h3>
                <p class="text-center">Come see us live! Book your tickets!</p>
                <ul class="list-group">
                    <li class="list-group-item">May <span class="badge badge-danger">Sold Out!</span></li>
                    <li class="list-group-item">June <span class="badge badge-danger">Sold Out</span></li>
                    <li class="list-group-item">July <span class="badge badge-secondary">3</span></li>
                </ul>


                <div class="row text-center">
                    <div class="col-sm-4">
                        <div class="thumbnail">
                            <img src="paris.jpg" alt="Paris" width="400" height="300">
                            <p><strong>Paris</strong></p>
                            <p>27 July 2019</p>
                            <button class="btn" data-toggle="modal" data-target="#buyModal">Buy Tickets</button>
                        </div>
                    </div>

                    <div class="col-sm-4">
                        <div class="thumbnail">
                            <img src="newyork.jpg" alt="New York" width="400" height="300">
                            <p><strong>New York</strong></p>
                            <p>28 July 2019</p>
                            <button class="btn" data-toggle="modal" data-target="#buyModal">Buy Tickets</button>
                        </div>
                    </div>

                    <div class="col-sm-4">
                        <div class="thumbnail">
                            <img src="sanfran.jpg" alt="San Francisco" width="400" height="300">
                            <p><strong>San Francisco</strong></p>
                            <p>29 July 2019</p>
                            <button class="btn" data-toggle="modal" data-target="#buyModal">Buy Tickets</button>
                        </div>
                    </div>

                    <div class="modal fade" id="buyModal" role="dialog">
                        <div class="modal-dialog">
                            
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="close" data-dismiss="modal">&times;</button><br>
                                    <h4><span class="fa fa-lock"></span> Tickets</h4>
                                </div>

                                <div class="modal-body">
                                    <form role="form">
                                        <div class="form-group">
                                            <label for="psw"><span class="fa fa-shopping-cart"></span> Tickets, $20 per person.</label>
                                            <input type="number" class="form-control" id="psw" placeholder="How many?">
                                        </div>

                                        <div class="form-group">
                                            <label for="usrname"><span class="fa fa-user"></span> Send To</label>
                                            <input type="text" class="form-control" id="usrname" placeholder="Enter email">
                                        </div>

                                        <button type="submit" class="btn btn-block">Purchase <span class="fa fa-ok"></span></button>
                                    </form>
                                </div>

                                <div class="modal-footer">
                                    <button type="button" class="btn btn-danger btn-default pull-left" data-dismiss="modal">
                                        <span class="fa fa-remove"></span> Cancel
                                    </button>
                                    <p>Need <a href="">Help?</a></p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
        return navigation + slider + about + roster + tour

    def description(self):
        return self.__repr__
#endregion Band Template

#region Shop Template
class Shop(Section):
    def __init__(self):
        self.style = style
        self.js = js
        self.body = body
#endregion Shop Template
#endregion Templates

#region Footer
class Footer(Section):
    def __repr__(self):
        return "Footer"

    def content(self):
        return '''
<footer class="container-fluid text-center" style="background-color: #555; color: white; padding: 15px;">
    <p>Sitebuilder 1.0 | 2019</p>
</footer>
        '''

    def description(self):
        return "Bootstrap footer"
#endregion Footer
        
class BootstrapEnd(Section):
    def __repr__(self):
        return "Boostrap | Javascript"
        
    def content(self):
        return '''
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
'''

    def description(self):
        return "End of Bootstrap boilerplate code"