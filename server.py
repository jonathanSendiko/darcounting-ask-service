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
        logging.info(f"Received session: {request.session_id}")
        
        # Generate answer using AI service
        result = self.ai_service.generate_answer(
            question=request.question,
            session_id=request.session_id if request.session_id else None,
            context_tables=request.context_tables if request.context_tables else None
        )
        
        # Create response
        return qa_service_pb2.AnswerResponse(
            answer=result["answer"] or "",
            success=result["success"],
            error=result["error"] or "",
            confidence=result["confidence"]
        )
    
    def CreateSession(self, request, context):
        """Create a new chat session."""
        logging.info("Creating new chat session")
        try:
            session_id = self.ai_service.create_session()
            return qa_service_pb2.CreateSessionResponse(
                session_id=session_id,
                success=True,
                error=""
            )
        except Exception as e:
            error_msg = f"Failed to create session: {str(e)}"
            logging.error(error_msg)
            return qa_service_pb2.CreateSessionResponse(
                session_id="",
                success=False,
                error=error_msg
            )
    
    def DeleteSession(self, request, context):
        """Delete an existing chat session."""
        logging.info(f"Deleting session: {request.session_id}")
        success = self.ai_service.delete_session(request.session_id)
        
        if success:
            return qa_service_pb2.DeleteSessionResponse(
                success=True,
                error=""
            )
        else:
            error_msg = f"Failed to delete session: {request.session_id}"
            logging.error(error_msg)
            return qa_service_pb2.DeleteSessionResponse(
                success=False,
                error=error_msg
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