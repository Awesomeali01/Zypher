# Zypher

Zypher is a robust framework designed to accelerate the development of Flet applications. It simplifies project creation, integrates essential components, and provides a customizable routing system to streamline your workflow.

## Features

- **Interactive CLI**: Effortlessly create and manage Flet projects using an interactive command-line interface.
- **Template Support**: Choose from basic, advanced, and state-management templates to suit your project needs.
- **Authentication Integration**: Built-in support for authentication using Supabase (optional).
- **Component Libraries**:
  - AppBar
  - NavigationBar
- **Dynamic Routing**: Highly customizable routing system with error handling for undefined routes.
- **State Management**: Includes a simple state management system for global state handling.
- **Environment Support**: Easily switch between development and production environments.
- **Project Utilities**:
  - Build
  - Clean
  - Documentation Generation
- **Auto-Reload**: Enable auto-reload for smoother development workflows.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Awesomeali01/Zypher
   ```
2. Navigate to the project directory:
   ```bash
   cd Zypher
   ```
3. Install the package:
   ```bash
   pip install .
   ```

## Usage

### Creating a New Project

Use the interactive CLI to create a new project:
```bash
zypher create
```

### Serving a Project
Serve a project with auto-reload enabled:
```bash
zypher serve <project_dir> -r
```

### Building a Project
Build the project for deployment:
```bash
zypher build <project_dir>
```

### Cleaning a Project
Remove build artifacts:
```bash
zypher clean <project_dir>
```

### Generating Documentation
Generate project documentation:
```bash
zypher docs <project_dir>
```

## Project Structure

The framework creates a well-organized project structure:
```
project_name/
├── main.py
├── src/
│   ├── app.py
│   ├── components/
│   │   ├── appbar.py
│   │   └── navbar.py
│   ├── pages/
│   │   ├── home.py
│   │   ├── page1.py
│   │   ├── login.py (if auth enabled)
│   │   └── signup.py (if auth enabled)
│   ├── state/
│   │   └── store.py
│   └── utils/
│       ├── routes.py
│       └── supabase_client.py (if auth enabled)
└── tests/
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

Developed by **ALi Khan - The Space Dev**  
Email: ali.bgmi.in@gmail.com
