import grpc
from concurrent import futures
import qa_service_pb2
import qa_service_pb2_grpc
from ai_service import AIService
from config import Config
import logging

class QuestionAnswerer(qa_service_pb2_grpc.QuestionAnswererServicer):
    def __init__(self):
        self.ai_service = AIService()
    
    def AskQuestion(self, request, context):
        """Handle incoming question requests."""
        logging.info(f"Received question: {request.question}")
        
        # Generate answer using AI service
        result = self.ai_service.generate_answer(
            question=request.question,
            context_tables=request.context_tables if request.context_tables else None
        )
        
        # Create response
        return qa_service_pb2.AnswerResponse(
            answer=result["answer"] or "",
            success=result["success"],
            error=result["error"] or "",
            confidence=result["confidence"]
        )

def serve():
    """Start the gRPC server."""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Create server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    qa_service_pb2_grpc.add_QuestionAnswererServicer_to_server(
        QuestionAnswerer(), server
    )
    
    # Add secure credentials if needed (for production)
    server.add_insecure_port(f'{Config.SERVER_HOST}:{Config.SERVER_PORT}')
    
    # Start server
    server.start()
    logging.info(f"Server started on port {Config.SERVER_PORT}")
    
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve() 