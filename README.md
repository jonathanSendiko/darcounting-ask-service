# Darcounting Ask Service

A gRPC-based service that provides AI-powered question answering capabilities using OpenAI's GPT models.

## Features

- gRPC server implementation
- Integration with OpenAI's GPT models
- PostgreSQL database integration
- Configurable through environment variables

## Requirements

- Python 3.x
- PostgreSQL database
- OpenAI API key

## Setup

1. Clone the repository:
```bash
git clone [your-repo-url]
cd darcounting-ask-service
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Create a `.env` file in the project root with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
GPT_MODEL=gpt-4-1106-preview
POSTGRES_URI=your_postgres_connection_string
SERVER_HOST=[::]
SERVER_PORT=50051
MAX_TOKENS=4000
TEMPERATURE=0.7
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

[Add instructions for running the service]

## Contributing

[Add contribution guidelines]

## License

[Add license information] 