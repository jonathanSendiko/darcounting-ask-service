from openai import OpenAI
from config import Config
from database import DatabaseClient
from typing import Optional, List, Dict
import uuid

class AIService:
    def __init__(self):
        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY,
            base_url="https://api.openai.com/v1"
        )
        self.db_client = DatabaseClient()
        # Create sessions table if it doesn't exist
        self.db_client.create_sessions_table()
        
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

    def create_session(self) -> str:
        """Create a new chat session and return the session ID."""
        return str(self.db_client.create_session())

    def generate_answer(self, question: str, session_id: Optional[str] = None, context_tables: Optional[List[str]] = None) -> Dict:
        """Generate an answer to a question, optionally within a session context."""
        try:
            db_context = self.db_client.get_database_context(context_tables)
            messages = [{"role": "system", "content": self.generate_system_prompt(db_context)}]
            
            # If session_id is provided, get previous context
            if session_id:
                try:
                    uuid.UUID(session_id)  # Validate UUID format
                    context = self.db_client.get_session_context(session_id)
                    messages.extend(context)
                except ValueError:
                    return {
                        "answer": None,
                        "success": False,
                        "error": "Invalid session ID format",
                        "confidence": 0.0
                    }
            
            # Add the current question
            messages.append({"role": "user", "content": question})
            
            response = self.client.chat.completions.create(
                model=Config.GPT_MODEL,
                messages=messages,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            answer = response.choices[0].message.content
            
            # If within a session, update the context
            if session_id:
                messages.append({"role": "assistant", "content": answer})
                self.db_client.update_session_context(session_id, messages[1:])  # Exclude system prompt
            
            return {
                "answer": answer,
                "success": True,
                "error": None,
                "confidence": float(response.choices[0].finish_reason == "stop")
            }
            
        except Exception as e:
            return {
                "answer": None,
                "success": False,
                "error": str(e),
                "confidence": 0.0
            }
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a chat session."""
        try:
            uuid.UUID(session_id)  # Validate UUID format
            self.db_client.delete_session(session_id)
            return True
        except (ValueError, Exception):
            return False
    
    def close(self):
        self.db_client.close() 