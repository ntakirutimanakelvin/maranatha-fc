# Deploy Agent ntakirutimanakelvin

### Project Overview

This project is a Shell Scripting automation solution for the **Student Attendance Tracker** application. The script acts as a **Project Factory**, automatically creating the required project structure, configuring application settings, validating the environment, and handling unexpected interruptions through signal trapping.

---

## Features

### 1. Automated Project Setup

The script automatically creates a project workspace using a user-provided name.

Example:

```bash
attendance_tracker_schoolA
```
Generated structure:

```text
attendance_tracker_v1/
│
├── attendance_checker.py
│
├── Helpers/
│   ├── assets.csv
│   └── config.json
│
└── reports/
    └── reports.log
```

### 2. Dynamic Configuration

During setup, the script prompts the user to update attendance thresholds.

Default values:

| Setting           | Default |
| ----------------- | ------- |
| Warning Threshold | 75%     |
| Failure Threshold | 50%     |

The script uses:

```bash
read
```

to capture user input and

```bash
sed
```

to update values directly inside:

```text
Helpers/config.json
```

### 3. Environment Health Check

Before completing setup, the script verifies that Python is available on the system.

Command used:

```bash
python3 --version
```

It also validates that the required directory structure was successfully created.

### 4. Process Management (Signal Trap)

The script handles interruptions gracefully using trap and the handle_exit_signal function


## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/ntakirutimanakelvin/deploy_agent_ntakirutimanakelvin.git
```

### Step 2: Navigate into the Repository

```bash
cd deploy_agent_ntakirutimanakelvin
```

### Step 3: Make the Script Executable

```bash
chmod +x setup_project.sh
```

### Step 4: Run the Script

```bash
./setup_project.sh
```

---

### Step 5: To test the SIGINT trap functionality:

While the script is running, press:

```bash
CTRL + C
```

### The script should:

* Create an archive of the current project state.
* Delete the partially created project directory.
* Exit with a cleanup message.
