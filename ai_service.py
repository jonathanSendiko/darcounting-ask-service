from openai import OpenAI
from config import Config
from database import DatabaseClient

class AIService:
    def __init__(self):
        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY,
            base_url="https://api.openai.com/v1"
        )
        self.db_client = DatabaseClient()
        
    def generate_system_prompt(self, db_context):
        return f"""You are a helpful AI assistant that answers questions about data in a PostgreSQL database.
Below is the database schema and sample data:

{db_context}

Please provide accurate answers based on the database structure and sample data shown above.
If you need to make assumptions, please state them clearly.
If you cannot answer the question with the given information, please say so. 
Please provide the answer as if you are talking to a person without a technical background.
Do not say anything about the database schema or sample data in your answer.
Be concise and to the point except for when the question is about the sample data."""

    def generate_answer(self, question, context_tables=None):
        """Generate an answer to a question using GPT and database context."""
        try:
            # Get database context
            db_context = self.db_client.get_database_context(context_tables)
            
            # Create the conversation
            response = self.client.chat.completions.create(
                model=Config.GPT_MODEL,
                messages=[
                    {"role": "system", "content": self.generate_system_prompt(db_context)},
                    {"role": "user", "content": question}
                ],
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            # Extract the answer
            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "success": True,
                "error": None,
                "confidence": float(response.choices[0].finish_reason == "stop")  # 1.0 if completed normally
            }
            
        except Exception as e:
            return {
                "answer": None,
                "success": False,
                "error": str(e),
                "confidence": 0.0
            }
    
    def close(self):
        """Clean up resources."""
        self.db_client.close() 