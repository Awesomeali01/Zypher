# 🚀 Zypher

<div align="center">
*A powerful CLI tool for creating lightning-fast Flet applications with enterprise-grade features* ⚡
</div>

## ✨ Features

- 🎯 **Quick Project Setup** - Scaffold new projects in seconds
- 🛣️ **Smart Routing** - Built-in routing system with error handling
- 🔐 **Authentication Ready** - Optional Supabase integration
- 📱 **UI Components** - Pre-built AppBar & NavigationBar
- 🏗️ **Multiple Templates** - Basic, Advanced, and State Management
- 🔄 **Dev Tools** - Hot reload for rapid development
- 📚 **Auto Documentation** - Generate docs with one command
- 💾 **State Management** - Global store with persistence
- 🧪 **Testing Ready** - Pre-configured test environment

## 🛠️ Installation

0. Clone the repository:
```bash
git clone https://github.com/Awesomeali01/zypher
```

1. Navigate To Zypher
```bash
cd Zypher
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Install Zypher CLI tool:
```bash
pip install .
```

## 🚦 Quick Start

Create a new project with our interactive CLI:
```bash
zypher create
```

You'll be guided through choosing:
- 📂 Project name
- 🎨 Template type
- 🌍 Environment setup
- 🎯 UI components
- 🔑 Authentication options

## 📁 Project Structure

```
your-project/
├── 📄 main.py
├── 📂 src/
│   ├── 📱 app.py
│   ├── 🧩 components/
│   │   ├── appbar.py
│   │   └── navbar.py
│   ├── 📃 pages/
│   │   ├── home.py
│   │   └── page1.py
│   ├── 💾 state/
│   │   └── store.py
│   └── 🛠️ utils/
│       ├── routes.py
│       └── supabase_client.py
├── 🧪 tests/
└── 📝 .env
```

## 🎮 Available Commands

```bash
# Create new project
zypher create

# Serve with hot reload
zypher serve ./your-project -r

# Build project
zypher build ./your-project

# Generate docs
zypher docs ./your-project

# Clean artifacts
zypher clean ./your-project
```

## 🎨 Templates

### 🌱 Basic Template
Perfect for starting small with room to grow:
- Simple two-page setup
- Basic routing
- Optional components

### 🌟 Advanced Template
For feature-rich applications:
- Complex routing
- Extended UI components
- Enhanced features

### 💎 State Management Template
For data-intensive applications:
- Global store
- State persistence
- Action management

## 🔐 Authentication Setup

When authentication is enabled:

1. Create your Supabase project
2. Add credentials to `.env`:
```env
SUPABASE_URL=your-project-url
SUPABASE_ANON_KEY=your-anon-key
```

## 🛠️ Development

### Prerequisites
- 🐍 Python 3.7+
- 📦 pip package manager

### Required Packages
- 🎨 flet
- 🔑 python-dotenv
- 🔒 supabase

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/amazing-feature`)
3. 💫 Commit changes (`git commit -m 'Add amazing feature'`)
4. 🚀 Push to branch (`git push origin feature/amazing-feature`)
5. 🎯 Open a Pull Request

## 💫 Credits

Crafted with ❤️ by [Ali Khan](https://portfoalio.vercel.app) - The Space Dev 🚀

## 🌟 Support

Found a bug? Have a feature request? We'd love to hear from you:

- 🐛 [Report a bug](../../issues)
- 💡 [Request a feature](../../issues)
- 📧 [Email support](mailto:ali.bgmi.in@gmail.com)

---

<div align="center">
Made with 💜 and a lot of ☕
</div>