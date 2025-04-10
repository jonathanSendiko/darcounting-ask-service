# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import qa_service_pb2 as qa__service__pb2


class QuestionAnswererStub(object):
    """The question answering service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AskQuestion = channel.unary_unary(
                '/qa_service.QuestionAnswerer/AskQuestion',
                request_serializer=qa__service__pb2.QuestionRequest.SerializeToString,
                response_deserializer=qa__service__pb2.AnswerResponse.FromString,
                )
        self.CreateSession = channel.unary_unary(
                '/qa_service.QuestionAnswerer/CreateSession',
                request_serializer=qa__service__pb2.CreateSessionRequest.SerializeToString,
                response_deserializer=qa__service__pb2.CreateSessionResponse.FromString,
                )
        self.DeleteSession = channel.unary_unary(
                '/qa_service.QuestionAnswerer/DeleteSession',
                request_serializer=qa__service__pb2.DeleteSessionRequest.SerializeToString,
                response_deserializer=qa__service__pb2.DeleteSessionResponse.FromString,
                )


class QuestionAnswererServicer(object):
    """The question answering service definition
    """

    def AskQuestion(self, request, context):
        """Send a question and receive an answer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSession(self, request, context):
        """Create a new chat session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSession(self, request, context):
        """Delete an existing chat session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuestionAnswererServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AskQuestion': grpc.unary_unary_rpc_method_handler(
                    servicer.AskQuestion,
                    request_deserializer=qa__service__pb2.QuestionRequest.FromString,
                    response_serializer=qa__service__pb2.AnswerResponse.SerializeToString,
            ),
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=qa__service__pb2.CreateSessionRequest.FromString,
                    response_serializer=qa__service__pb2.CreateSessionResponse.SerializeToString,
            ),
            'DeleteSession': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSession,
                    request_deserializer=qa__service__pb2.DeleteSessionRequest.FromString,
                    response_serializer=qa__service__pb2.DeleteSessionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qa_service.QuestionAnswerer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class QuestionAnswerer(object):
    """The question answering service definition
    """

    @staticmethod
    def AskQuestion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qa_service.QuestionAnswerer/AskQuestion',
            qa__service__pb2.QuestionRequest.SerializeToString,
            qa__service__pb2.AnswerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qa_service.QuestionAnswerer/CreateSession',
            qa__service__pb2.CreateSessionRequest.SerializeToString,
            qa__service__pb2.CreateSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qa_service.QuestionAnswerer/DeleteSession',
            qa__service__pb2.DeleteSessionRequest.SerializeToString,
            qa__service__pb2.DeleteSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
