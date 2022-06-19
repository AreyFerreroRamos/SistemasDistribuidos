# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import functions_pb2 as functions__pb2


class FunctionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddInsult = channel.unary_unary(
                '/Functions/AddInsult',
                request_serializer=functions__pb2.Insult.SerializeToString,
                response_deserializer=functions__pb2.Empty.FromString,
                )
        self.GetInsults = channel.unary_unary(
                '/Functions/GetInsults',
                request_serializer=functions__pb2.Empty.SerializeToString,
                response_deserializer=functions__pb2.Insults.FromString,
                )
        self.Insultme = channel.unary_unary(
                '/Functions/Insultme',
                request_serializer=functions__pb2.Empty.SerializeToString,
                response_deserializer=functions__pb2.Insult.FromString,
                )


class FunctionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddInsult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInsults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insultme(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FunctionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddInsult': grpc.unary_unary_rpc_method_handler(
                    servicer.AddInsult,
                    request_deserializer=functions__pb2.Insult.FromString,
                    response_serializer=functions__pb2.Empty.SerializeToString,
            ),
            'GetInsults': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInsults,
                    request_deserializer=functions__pb2.Empty.FromString,
                    response_serializer=functions__pb2.Insults.SerializeToString,
            ),
            'Insultme': grpc.unary_unary_rpc_method_handler(
                    servicer.Insultme,
                    request_deserializer=functions__pb2.Empty.FromString,
                    response_serializer=functions__pb2.Insult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Functions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Functions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddInsult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Functions/AddInsult',
            functions__pb2.Insult.SerializeToString,
            functions__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInsults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Functions/GetInsults',
            functions__pb2.Empty.SerializeToString,
            functions__pb2.Insults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insultme(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Functions/Insultme',
            functions__pb2.Empty.SerializeToString,
            functions__pb2.Insult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
