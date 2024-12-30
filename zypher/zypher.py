# zypher/zypher.py
import os
import click
import inquirer
import shutil
import subprocess

@click.group()
def cli():
    pass

def create_project(project_name, template, env, appbar, navigation_bar, auth):
    """
    Create a new Flet project with a robust and customizable routing system.
    """
    project_dir = os.path.join(os.getcwd(), project_name)
    
    if os.path.exists(project_dir):
        click.echo(f"Project directory '{project_dir}' already exists.")
        return

    os.makedirs(project_dir)
    os.makedirs(os.path.join(project_dir, 'src'))
    os.makedirs(os.path.join(project_dir, 'src', 'components'))
    os.makedirs(os.path.join(project_dir, 'src', 'pages'))
    os.makedirs(os.path.join(project_dir, 'src', 'state'))
    os.makedirs(os.path.join(project_dir, 'src', 'utils'))
    os.makedirs(os.path.join(project_dir, 'tests'))

    # Create main.py
    with open(os.path.join(project_dir, 'main.py'), 'w') as f:
        f.write(f"""
import flet as ft
from src.app import App

def main(page: ft.Page):
    app = App(page, auth={auth})
    app.run()

if __name__ == "__main__":
    ft.app(target=main)
""")

    # Create app.py in the src directory
    with open(os.path.join(project_dir, 'src', 'app.py'), 'w') as f:
        f.write("""
import flet as ft
from src.state import store
from src.utils import routes

class App:
    def __init__(self, page: ft.Page, auth: bool):
        self.page = page
        self.page.title = "Flet App"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.on_route_change = self.route_change
        
        # Modify auth check
        if auth:
            # Check if you want to enforce authentication
            # For local dev, you might want to skip
            from src.utils.supabase_client import supabase_client
            if supabase_client is None:
                self.page.go("/")
            else:
                self.page.go("/login")
        else:
            self.page.go("/")
        
        self.page.update()
        
    def route_change(self, route):
        self.page.views.clear()
        route = self.page.route
        if route in routes.ROUTES:
            self.page.views.append(routes.ROUTES[route](page=self.page))
        else:
            self.page.views.append(routes.not_found(page=self.page))
        self.page.update()

    def run(self):
        self.page.update()
""")

    # Create routes.py in the utils directory
    with open(os.path.join(project_dir, 'src', 'utils', 'routes.py'), 'w') as f:
        routes_content = """
import flet as ft
from src.pages.home import home
from src.pages.page1 import page1
"""

        if auth:
            routes_content += """
from src.pages.login import login
from src.pages.signup import signup
"""

        routes_content += """
ROUTES = {
    "/": home,
    "/page1": page1,
"""

        if auth:
            routes_content += """
    "/login": login,
    "/signup": signup,
"""

        routes_content += """
}

NAVIGATION_ITEMS = [
    {"icon": ft.icons.HOME, "label": "Home", "route": "/"},
    {"icon": ft.icons.EXPLORE, "label": "Page 1", "route": "/page1"},
]

def not_found(page: ft.Page):
    return ft.View(
        "/404",
        [ft.Text("404: Not Found", size=24)],
    )
"""

        f.write(routes_content)

    # Create navbar.py in the components directory
    with open(os.path.join(project_dir, 'src', 'components', 'navbar.py'), 'w') as f:
        f.write("""
import flet as ft
from src.utils import routes

def create_navbar(page: ft.Page):
    destinations = [
        ft.NavigationDestination(icon=item["icon"], label=item["label"])
        for item in routes.NAVIGATION_ITEMS
    ]
    return ft.NavigationBar(
        destinations=destinations,
        on_change=lambda e: handle_navigation_change(e, page, routes.NAVIGATION_ITEMS)
    )

def handle_navigation_change(e, page, navigation_items):
    selected_index = e.control.selected_index
    if 0 <= selected_index < len(navigation_items):
        route = navigation_items[selected_index]["route"]
        page.go(route)
    page.update()
""")

    # Create appbar.py in the components directory
    with open(os.path.join(project_dir, 'src', 'components', 'appbar.py'), 'w') as f:
        f.write("""
import flet as ft

def create_appbar(page: ft.Page):
    return ft.AppBar(
        title=ft.Text("Flet App"),
        actions=[
            ft.IconButton(ft.icons.SEARCH, on_click=lambda _: print("Search clicked")),
            ft.IconButton(ft.icons.NOTIFICATIONS, on_click=lambda _: print("Notifications clicked")),
        ]
    )
""")

    # Create home.py in the pages directory
    with open(os.path.join(project_dir, 'src', 'pages', 'home.py'), 'w') as f:
        f.write(f"""
import flet as ft
{'from src.components.appbar import create_appbar' if appbar else ''}
{'from src.components.navbar import create_navbar' if navigation_bar else ''}

def home(page: ft.Page):
    components = []
    {'components.append(create_appbar(page))' if appbar else ''}
    {'components.append(create_navbar(page))' if navigation_bar else ''}
    components.append(ft.ElevatedButton("Go to Page 1", on_click=lambda _: page.go("/page1")))
    return ft.View(
        "/",
        components,
    )
""")

    # Create page1.py in the pages directory
    with open(os.path.join(project_dir, 'src', 'pages', 'page1.py'), 'w') as f:
        f.write(f"""
import flet as ft
{'from src.components.appbar import create_appbar' if appbar else ''}
{'from src.components.navbar import create_navbar' if navigation_bar else ''}

def page1(page: ft.Page):
    components = []
    {'components.append(create_appbar(page))' if appbar else ''}
    {'components.append(create_navbar(page))' if navigation_bar else ''}
    components.append(ft.ElevatedButton("Go to Home", on_click=lambda _: page.go("/")))
    return ft.View(
        "/page1",
        components,
    )
""")

    if auth:
        # Create login.py in the pages directory
        with open(os.path.join(project_dir, 'src', 'pages', 'login.py'), 'w') as f:
            f.write("""
import flet as ft
from src.utils.supabase_client import supabase_client

def login(page: ft.Page):
    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    error_message = ft.Text(value="", color="red", visible=False)

    def handle_login(e):  # Changed to accept event parameter
        email_value = email.value
        password_value = password.value
        if not email_value or not password_value:
            error_message.value = "Email and password are required."
            error_message.visible = True
            page.update()
            return

        # If supabase_client is None, just simulate login for testing
        if supabase_client is None:
            page.go("/")
            return

        try:
            # Adjust based on actual Supabase SDK method
            response = supabase_client.auth.sign_in_with_password({"email": email_value, "password": password_value})
            # Handle response based on Supabase SDK
            page.go("/")
        except Exception as e:
            error_message.value = f"An error occurred: {str(e)}"
            error_message.visible = True
        finally:
            page.update()

    login_button = ft.ElevatedButton("Login", on_click=handle_login)
    forget_password = ft.TextButton("Forgot Password?", on_click=lambda _: page.go("/forgot-password"))

    return ft.View(
        "/login",
        [
            ft.Text("Login", size=24),
            email,
            password,
            login_button,
            forget_password,
            error_message,
        ],
    )
""")

        # Create signup.py in the pages directory
        with open(os.path.join(project_dir, 'src', 'pages', 'signup.py'), 'w') as f:
            f.write("""
import flet as ft
from src.utils.supabase_client import supabase_client

def signup(page: ft.Page):
    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    signup_button = ft.ElevatedButton("Sign Up", on_click=lambda _: handle_signup(page, email, password))
    error_message = ft.Text(value="", color="red", visible=False)

    def handle_signup(event):
        email_value = email.value
        password_value = password.value
        if not email_value or not password_value:
            error_message.value = "Email and password are required."
            error_message.visible = True
            page.update()
            return

        try:
            response = supabase_client.auth.sign_up(email=email_value, password=password_value)
            error = response.get("error")
            if error:
                error_message.value = error.message
                error_message.visible = True
            else:
                error_message.visible = False
                page.go("/login")
        except Exception as e:
            error_message.value = f"An error occurred: {str(e)}"
            error_message.visible = True
        finally:
            page.update()

    return ft.View(
        "/signup",
        [
            ft.Text("Sign Up", size=24),
            email,
            password,
            signup_button,
            error_message,
        ],
    )
""")

        # Create supabase_client.py in the utils directory
        with open(os.path.join(project_dir, 'src', 'utils', 'supabase_client.py'), 'w') as f:
            f.write("""
import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")

# Only create client if credentials are provided
supabase_client = None
if SUPABASE_URL and SUPABASE_ANON_KEY:
    supabase_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
""")

        # Create .env file
        with open(os.path.join(project_dir, '.env'), 'w') as f:
            f.write("""
SUPABASE_URL=
SUPABASE_ANON_KEY=
""")

    # Create store.py in the state directory
    with open(os.path.join(project_dir, 'src', 'state', 'store.py'), 'w') as f:
        f.write("""
class Store:
    def __init__(self):
        self.state = {}

    def get_state(self, key):
        return self.state.get(key)

    def set_state(self, key, value):
        self.state[key] = value

store = Store()
""")

    # Create README.md in the project directory
    with open(os.path.join(project_dir, 'README.md'), 'w') as f:
        f.write(f"""
# {project_name}

## Description
This is a Flet project created using the Zypher framework.

## Setup
1. Install Flet: `pip install flet`
2. Install Supabase client: `pip install supabase`
3. Install python-dotenv: `pip install python-dotenv`
4. Run the project: `flet run main.py`

## Templates
- **basic**: Basic template with home and page1.
- **advanced**: Advanced template with more features.
- **state-management**: Template with state management.

## Environment
- **development**: Development environment.
- **production**: Production environment.

## Components
- AppBar
- NavigationBar

## Build System
To build the project, run: `zypher build .`

## Documentation
To generate documentation, run: `zypher docs .`

## Clean
To clean the project, run: `zypher clean .`
""")

    click.echo(f"🎉 Project '{project_name}' created successfully with the '{template}' template and '{env}' environment. 🎉")

@cli.command()
def create():
    """
    Create a new Flet project with an interactive setup.
    """
    questions = [
        inquirer.Text('project_name', message="Enter the project name"),
        inquirer.List('template', message="Choose a template", choices=['basic', 'advanced', 'state-management'], default='basic'),
        inquirer.List('env', message="Choose an environment", choices=['development', 'production'], default='development'),
        inquirer.Confirm('appbar', message="Do you want to include an AppBar component?", default=True),
        inquirer.Confirm('navigation_bar', message="Do you want to include a NavigationBar component?", default=True),
        inquirer.Confirm('auth', message="Do you want to include authentication?", default=False),
    ]

    answers = inquirer.prompt(questions)

    create_project(
        project_name=answers['project_name'],
        template=answers['template'],
        env=answers['env'],
        appbar=answers['appbar'],
        navigation_bar=answers['navigation_bar'],
        auth=answers['auth']
    )

@cli.command()
@click.argument('project_dir')
@click.option('-r', '--auto-reload', is_flag=True, help='Enable auto-reload for development')
def serve(project_dir, auto_reload):
    """
    Serve the Flet project.
    """
    main_path = os.path.join(project_dir, 'main.py')
    if not os.path.exists(main_path):
        click.echo(f"main.py not found in '{project_dir}'.")
        return

    if auto_reload:
        os.system(f'flet run -r {main_path}')
    else:
        os.system(f'python {main_path}')

@cli.command()
@click.argument('project_dir')
def build(project_dir):
    """
    Build the Flet project.
    """
    click.echo(f"Building project in '{project_dir}'...")
    # Basic build logic (e.g., compile assets, minify code)
    subprocess.run(['python', '-m', 'compileall', project_dir])
    click.echo("Build completed.")

@cli.command()
@click.argument('project_dir')
def clean(project_dir):
    """
    Clean the project (e.g., remove build artifacts).
    """
    click.echo(f"Cleaning project in '{project_dir}'...")
    # Basic clean logic (e.g., remove build directories, cache files)
    build_dir = os.path.join(project_dir, '__pycache__')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    click.echo("Clean completed.")

@cli.command()
@click.argument('project_dir')
def docs(project_dir):
    """
    Generate documentation for the project.
    """
    click.echo(f"Generating documentation for project in '{project_dir}'...")
    # Run Sphinx
    subprocess.run(['sphinx-build', '-b', 'html', os.path.join(project_dir, 'docs'), os.path.join(project_dir, 'docs', '_build')])
    click.echo("Documentation generated.")

if __name__ == "__main__":
    cli()