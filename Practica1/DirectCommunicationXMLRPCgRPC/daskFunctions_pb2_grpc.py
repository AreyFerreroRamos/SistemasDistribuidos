# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import daskFunctions_pb2 as daskFunctions__pb2


class DaskFunctionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadCSV = channel.unary_unary(
                '/DaskFunctions/ReadCSV',
                request_serializer=daskFunctions__pb2.NameFile.SerializeToString,
                response_deserializer=daskFunctions__pb2.FileReturn.FromString,
                )
        self.Max = channel.unary_unary(
                '/DaskFunctions/Max',
                request_serializer=daskFunctions__pb2.Field.SerializeToString,
                response_deserializer=daskFunctions__pb2.ValueReturn.FromString,
                )
        self.Min = channel.unary_unary(
                '/DaskFunctions/Min',
                request_serializer=daskFunctions__pb2.Field.SerializeToString,
                response_deserializer=daskFunctions__pb2.ValueReturn.FromString,
                )


class DaskFunctionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadCSV(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Max(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Min(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DaskFunctionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadCSV': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadCSV,
                    request_deserializer=daskFunctions__pb2.NameFile.FromString,
                    response_serializer=daskFunctions__pb2.FileReturn.SerializeToString,
            ),
            'Max': grpc.unary_unary_rpc_method_handler(
                    servicer.Max,
                    request_deserializer=daskFunctions__pb2.Field.FromString,
                    response_serializer=daskFunctions__pb2.ValueReturn.SerializeToString,
            ),
            'Min': grpc.unary_unary_rpc_method_handler(
                    servicer.Min,
                    request_deserializer=daskFunctions__pb2.Field.FromString,
                    response_serializer=daskFunctions__pb2.ValueReturn.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DaskFunctions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DaskFunctions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadCSV(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DaskFunctions/ReadCSV',
            daskFunctions__pb2.NameFile.SerializeToString,
            daskFunctions__pb2.FileReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Max(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DaskFunctions/Max',
            daskFunctions__pb2.Field.SerializeToString,
            daskFunctions__pb2.ValueReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Min(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DaskFunctions/Min',
            daskFunctions__pb2.Field.SerializeToString,
            daskFunctions__pb2.ValueReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
