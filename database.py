import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

class DatabaseClient:
    def __init__(self):
        self.conn = psycopg2.connect(Config.POSTGRES_URI)
        
    def get_table_schema(self, table_name):
        """Get the schema of a specific table."""
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = %s;
            """, (table_name,))
            return cur.fetchall()
    
    def get_table_sample(self, table_name, limit=5):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(f"SELECT * FROM {table_name} LIMIT %s;", (limit,))
            return cur.fetchall()
    
    def execute_query(self, query, params=None):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params or ())
            return cur.fetchall()
    
    def get_available_tables(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public';
            """)
            return [row[0] for row in cur.fetchall()]
    
    def get_database_context(self, tables=None):
        context = []
        
        if not tables:
            tables = self.get_available_tables()
        
        for table in tables:
            schema = self.get_table_schema(table)
            schema_str = f"Table '{table}' schema:\n"
            for col in schema:
                schema_str += f"- {col[0]} ({col[1]}, Nullable: {col[2]})\n"
            
            samples = self.get_table_sample(table)
            sample_str = f"\nSample data from '{table}':\n"
            for sample in samples:
                sample_str += f"- {str(sample)}\n"
            
            context.append(schema_str + sample_str)
        
        return "\n".join(context)
    
    def create_sessions_table(self):
        """Create the sessions table if it doesn't exist."""
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    context TEXT[]
                );
            """)
            self.conn.commit()

    def create_session(self):
        """Create a new chat session and return the session ID."""
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO sessions (context) 
                VALUES (ARRAY[]::TEXT[]) 
                RETURNING session_id;
            """)
            self.conn.commit()
            return cur.fetchone()[0]

    def get_session_context(self, session_id):
        """Get the context for a specific session."""
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT context 
                FROM sessions 
                WHERE session_id = %s;
            """, (session_id,))
            result = cur.fetchone()
            return result[0] if result else []

    def update_session_context(self, session_id, new_context):
        """Update the context for a specific session."""
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE sessions 
                SET context = %s, 
                    last_updated = CURRENT_TIMESTAMP 
                WHERE session_id = %s;
            """, (new_context, session_id))
            self.conn.commit()

    def delete_session(self, session_id):
        """Delete a specific session."""
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM sessions 
                WHERE session_id = %s;
            """, (session_id,))
            self.conn.commit()

    def close(self):
        self.conn.close() 