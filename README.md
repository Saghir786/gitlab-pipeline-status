# GitLab Pipeline Status App

A Flask application to display the status of GitLab pipeline stages dynamically. The app supports updating the pipeline ID via a form and provides auto-refresh functionality to show real-time updates.

## Features

- **Dynamic Pipeline Status**: Displays the statuses for stages (`validate`, `plan`, `apply`, `destroy`) of a GitLab pipeline.
- **Pipeline ID Input**: Allows the user to change the pipeline ID on the fly.
- **Error Handling**: Neatly displays HTTP error codes for inaccessible or invalid pipelines.
- **Auto Refresh**: Updates statuses every 5 seconds.
- **Environment Variables**: Configurable using `PROJECT_ID`, `PIPELINE_ID`, and `ACCESS_TOKEN`.

## Getting Started

### Prerequisites

1. **Python**: Ensure Python 3.8 or later is installed.
2. **GitLab Access Token**: Create a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) with `read_api` scope.

### Installation

1. Clone the repository:
   ```bash
   git clone  https://github.com/Saghir786/gitlab-pipeline-status.git
   cd gitlab-pipeline-status
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   export PROJECT_ID="your-project-id-or-path"
   export PIPELINE_ID="123456"
   export ACCESS_TOKEN="your-access-token"
   ```

### Running the App

Start the Flask app:
```bash
python app.py
```

Access the app in your browser:
```
http://127.0.0.1:8080/
```

### Usage

1. Enter a GitLab pipeline ID in the input field to display its status.
2. If the pipeline is inaccessible or invalid, the app will show the corresponding HTTP status code.

## Project Structure

```
gitlab-pipeline-status/
├── app.py                # Main Flask application
├── templates/
│   └── pipeline.html     # HTML template
├── static/               # Static files (if needed)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Environment Variables

| Variable       | Description                     |
|----------------|---------------------------------|
| `PROJECT_ID`   | GitLab project ID or path       |
| `PIPELINE_ID`  | Initial pipeline ID             |
| `ACCESS_TOKEN` | GitLab Personal Access Token    |

## Contributing

Feel free to fork the repository and submit pull requests for new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
