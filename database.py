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
        """Get a sample of records from a table."""
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(f"SELECT * FROM {table_name} LIMIT %s;", (limit,))
            return cur.fetchall()
    
    def execute_query(self, query, params=None):
        """Execute a custom SQL query."""
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params or ())
            return cur.fetchall()
    
    def get_available_tables(self):
        """Get list of available tables in the database."""
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public';
            """)
            return [row[0] for row in cur.fetchall()]
    
    def get_database_context(self, tables=None):
        """Get comprehensive database context for AI processing."""
        context = []
        
        # If no specific tables are provided, get all tables
        if not tables:
            tables = self.get_available_tables()
        
        for table in tables:
            # Get schema information
            schema = self.get_table_schema(table)
            schema_str = f"Table '{table}' schema:\n"
            for col in schema:
                schema_str += f"- {col[0]} ({col[1]}, Nullable: {col[2]})\n"
            
            # Get sample data
            samples = self.get_table_sample(table)
            sample_str = f"\nSample data from '{table}':\n"
            for sample in samples:
                sample_str += f"- {str(sample)}\n"
            
            context.append(schema_str + sample_str)
        
        return "\n".join(context)
    
    def close(self):
        """Close the database connection."""
        self.conn.close() 